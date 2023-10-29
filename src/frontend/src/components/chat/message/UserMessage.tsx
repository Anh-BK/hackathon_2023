import { Card, CardBody, Textarea } from "@nextui-org/react";

import Markdown from "react-markdown";
import React from "react";
import remarkGfm from "remark-gfm";

export function UserMessage({ message }) {
  return (
    <Card>
      <CardBody className="py-4 justify-end">
        <Markdown className="text-[14px] p-0" remarkPlugins={[remarkGfm]}>
          {message.message}
        </Markdown>
        {/* <p className="text-[14px] p-0">{message}</p> */}
      </CardBody>
    </Card>
  );
}
