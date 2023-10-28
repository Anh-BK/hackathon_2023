import React from "react";

export function LoadingMessage() {
  return (
    <div className="flex gap-x-[2px]">
      <div className="bg-gray-400 w-[6px] h-[6px] flex items-center rounded-full animate-bounce first-circle"></div>
      <div className="bg-gray-400 w-[6px] h-[6px] flex items-center rounded-full animate-bounce second-circle"></div>
      <div className="bg-gray-400 w-[6px] h-[6px] flex items-center rounded-full animate-bounce third-circle"></div>
    </div>
  );
}
