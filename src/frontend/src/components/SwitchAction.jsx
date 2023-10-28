import { Checkbox, CheckboxGroup, Image, Switch } from "@nextui-org/react";

import React from "react";

export function SwitchAction({
  name,
  defaultSelected,
  preAction,
  setPreAction,
  valueAction,
}) {
  const onChange = (value) => {
    if (value) {
      setPreAction(valueAction);
      return;
    }
    setPreAction(null);
  };

  return (
    <Switch
      isDisabled={preAction !== null && preAction !== valueAction}
      color="default"
      defaultSelected={defaultSelected}
      onValueChange={onChange}
    >
      <p>{name}</p>
    </Switch>
  );
}
