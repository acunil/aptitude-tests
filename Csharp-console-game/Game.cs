using System;

namespace ConsoleGame
{
  class Game : SuperGame
  {
    public new static void UpdatePosition(string key, out int x, out int y)
    {
      x = 0;
      y = 0;
      switch (key)
      {
        case "DownArrow":
          y = 1;
          break;
        case "UpArrow":
          y = -1;
          break;
        case "RightArrow":
          x = 1;
          break;
        case "LeftArrow":
          x = -1;
          break;
      }
      
    }

    public new static char UpdateCursor(string key)
    {
      switch (key)
      {
        case "DownArrow":
          return 'v';
        case "UpArrow":
          return '^';
        case "RightArrow":
          return '>';
        case "LeftArrow":
          return '<';
        default:
          return '+';
      }
    }

    public new static int KeepInBounds(int coord, int max)
    {
      if (coord < 0)
      {
        return max;
      }
      else if (coord >= max)
      {
        return 0;
      }
      else
      {
        return coord;
      }
    }

    public new static bool DidScore(int char_x, int char_y, int fruit_x, int fruit_y)
    {
      return char_x == fruit_x && char_y == fruit_y;
    }
  }
}