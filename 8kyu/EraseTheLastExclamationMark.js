/**
Description:
Remove all exclamation marks from the end of sentence.

Examples
"Hi!"     ---> "Hi"
"Hi!!!"   ---> "Hi"
"!Hi"     ---> "!Hi"
"!Hi!"    ---> "!Hi"
"Hi! Hi!" ---> "Hi! Hi"
"Hi"      ---> "Hi"
 */

function EraseTheLastExclamationMark(string) {
  return string.replaceAll(/!+$/g, '');
}

function doTest(answer, result) {
  console.log(answer === result);
}

doTest(EraseTheLastExclamationMark('Hi!'), 'Hi');
doTest(EraseTheLastExclamationMark('Hi!!!'), 'Hi');
doTest(EraseTheLastExclamationMark('!Hi'), '!Hi');
doTest(EraseTheLastExclamationMark('!Hi!'), '!Hi');
doTest(EraseTheLastExclamationMark('Hi! Hi!'), 'Hi! Hi');
doTest(EraseTheLastExclamationMark('Hi'), 'Hi');
