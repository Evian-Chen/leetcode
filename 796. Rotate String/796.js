/**
 * @param {string} s
 * @param {string} goal
 * @return {boolean}
 */
var rotateString = function (s, goal) {
  if (s.length !== goal.length) return false;

  let aaa = s + s; //abcdeabcde
  return aaa.includes(goal);
};
