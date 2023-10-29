import { Avatar, Button, Card, CardBody, Textarea } from "@nextui-org/react";
import React, { useState } from "react";

import { AiFillDelete } from "react-icons/ai";
import Markdown from "react-markdown";
import { MdAddToPhotos } from "react-icons/md";
import axiosClient from "../../../config/axios";
import remarkGfm from "remark-gfm";

export function AIMessage({ message, getListMessage, getListUsefulMessage }) {
  const onAdd = async () => {
    await axiosClient.request({
      method: "POST",
      url: "/conversation/update_status",
      data: {
        message_id: message._id,
        is_useful: !message.is_useful,
      },
    });
    getListMessage();
    getListUsefulMessage();
  };

  return (
    <div className="flex items-center">
      <Avatar
        className="h-8 w-8"
        isBordered
        radius="full"
        src="https://www.the-digital-insurer.com/wp-content/uploads/2016/06/718RobotFinance.jpg"
      />
      <div className="group flex items-center justify-center">
        <Card className="mx-4 w-[400px]">
          <CardBody className="py-4">
            <Markdown className="text-[14px] p-0" remarkPlugins={[remarkGfm]}>
              {message.message}
            </Markdown>
            <br />
            <Markdown className="text-[14px] p-0" remarkPlugins={[remarkGfm]}>
              {message.citations}
            </Markdown>
            {/* <p className="text-[14px] p-0">{message}</p> */}
          </CardBody>
        </Card>
        <div className="hidden group-hover:block">
          <Button
            isIconOnly
            className="rounded-full bg-[#18181B]"
            onClick={onAdd}
          >
            {!message.is_useful ? <MdAddToPhotos /> : <AiFillDelete />}
          </Button>
        </div>
      </div>
    </div>
  );
}
