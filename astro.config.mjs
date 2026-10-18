import { defineConfig } from 'astro/config';

const pseudocodeLanguage = {
  name: 'pseudocode',
  scopeName: 'source.pseudocode',
  patterns: [
    { include: '#comments' },
    { include: '#strings' },
    { include: '#keywords' },
    { include: '#operators' },
    { include: '#types' },
    { include: '#constants' },
    { include: '#numbers' },
  ],
  repository: {
    comments: {
      patterns: [{ name: 'comment.line.double-slash.pseudocode', match: '//.*$' }],
    },
    strings: {
      patterns: [{ name: 'string.quoted.double.pseudocode', begin: '"', end: '"' }],
    },
    keywords: {
      patterns: [{
        name: 'keyword.control.pseudocode',
        match: '\\b(?:DECLARE|CONSTANT|INPUT|OUTPUT|IF|THEN|ELSE|ELSEIF|ENDIF|CASE|OF|OTHERWISE|ENDCASE|FOR|TO|STEP|NEXT|WHILE|DO|ENDWHILE|REPEAT|UNTIL|PROCEDURE|ENDPROCEDURE|FUNCTION|ENDFUNCTION|RETURN|CALL)\\b',
      }],
    },
    operators: {
      patterns: [{
        name: 'keyword.operator.pseudocode',
        match: '\\b(?:AND|OR|NOT|MOD|DIV)\\b',
      }],
    },
    types: {
      patterns: [{
        name: 'support.type.pseudocode',
        match: '\\b(?:INTEGER|REAL|STRING|CHAR|BOOLEAN)\\b',
      }],
    },
    constants: {
      patterns: [{ name: 'constant.language.pseudocode', match: '\\b(?:TRUE|FALSE)\\b' }],
    },
    numbers: {
      patterns: [{ name: 'constant.numeric.pseudocode', match: '\\b\\d+(?:\\.\\d+)?\\b' }],
    },
  },
};

function remarkCallouts() {
  return (tree) => {
    function visit(node) {
      if (!Array.isArray(node.children)) return;

      if (node.type === 'blockquote') {
        const firstParagraph = node.children[0];
        const marker = firstParagraph?.type === 'paragraph'
          ? firstParagraph.children?.map((child) => child.value ?? '').join('').match(/^\[!(NOTE|TIP|WARNING|CHALLENGE)\]$/i)
          : null;

        if (marker) {
          const type = marker[1].toLowerCase();
          const label = type[0].toUpperCase() + type.slice(1);
          firstParagraph.children = [{
            type: 'strong',
            children: [{ type: 'text', value: label }],
          }];
          node.data = {
            ...node.data,
            hProperties: {
              ...node.data?.hProperties,
              className: ['callout', `callout-${type}`],
            },
          };
        }
      }

      node.children.forEach(visit);
    }

    visit(tree);
  };
}

export default defineConfig({
  output: 'static',
  markdown: {
    remarkPlugins: [remarkCallouts],
    shikiConfig: {
      langs: [pseudocodeLanguage],
    },
  },
});