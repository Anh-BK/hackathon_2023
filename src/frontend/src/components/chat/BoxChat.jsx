import { ASSISTANT, USER } from "../../constants/role";
import { Button, Textarea } from "@nextui-org/react";
import React, { useState } from "react";

import { IoMdSend } from "react-icons/io";
import axiosClient from "../../config/axios";

export function BoxChat({ listMessage, setListMessage, company, preAction }) {
  const [message, setMessage] = useState(null);

  const sendMessage = async () => {
    if (!message) {
      return;
    }

    setListMessage((prevState) => [
      ...prevState,
      {
        message: message,
        role: USER,
      },
      {
        loading: true,
        role: ASSISTANT,
      },
    ]);

    const answer = await axiosClient.request({
      url: "/answering/answering",
      method: "POST",
      data: {
        human_message: message,
        company_name: company,
        history: [],
        task: preAction,
      },
    });

    setListMessage((prevState) => {
      if (prevState[prevState.length - 1].loading == false) {
        const newState = [
          ...prevState,
          {
            message: answer.answer,
            citations: answer.citation,
            role: ASSISTANT,
          },
        ];
        return newState;
      }
      const newState = [...prevState];
      newState[newState.length - 1] = {
        message: answer.answer,
        citations: answer.citation,
        role: ASSISTANT,
      };
      return newState;
    });

    setMessage("");
  };

  return (
    <div className="flex gap-x-2 items-center">
      <Textarea
        value={message}
        onValueChange={(value) => setMessage(value)}
        rows={4}
        variant="faded"
        labelPlacement="outside"
        placeholder="Enter your description"
        className="col-span-12 md:col-span-6 mb-6 md:mb-0"
      />
      <Button isIconOnly onClick={sendMessage}>
        <IoMdSend />
      </Button>
    </div>
  );
}
