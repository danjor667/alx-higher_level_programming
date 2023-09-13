#!/us/bin/node
const Rectangle = ('./4-rectangle').Rectangle;
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
