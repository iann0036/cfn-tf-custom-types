# TF::FortiOS::SwitchcontrollerLocation

Configure FortiSwitch location services.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::SwitchcontrollerLocation",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#addresscivic" title="AddressCivic">AddressCivic</a>" : <i>[ <a href="addresscivicdefinition.md">AddressCivicDefinition</a>, ... ]</i>,
        "<a href="#coordinates" title="Coordinates">Coordinates</a>" : <i>[ <a href="coordinatesdefinition.md">CoordinatesDefinition</a>, ... ]</i>,
        "<a href="#elinnumber" title="ElinNumber">ElinNumber</a>" : <i>[ <a href="elinnumberdefinition.md">ElinNumberDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::SwitchcontrollerLocation
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#addresscivic" title="AddressCivic">AddressCivic</a>: <i>
      - <a href="addresscivicdefinition.md">AddressCivicDefinition</a></i>
    <a href="#coordinates" title="Coordinates">Coordinates</a>: <i>
      - <a href="coordinatesdefinition.md">CoordinatesDefinition</a></i>
    <a href="#elinnumber" title="ElinNumber">ElinNumber</a>: <i>
      - <a href="elinnumberdefinition.md">ElinNumberDefinition</a></i>
</pre>

## Properties

#### Name

Unique location item name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AddressCivic

_Required_: No

_Type_: List of <a href="addresscivicdefinition.md">AddressCivicDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Coordinates

_Required_: No

_Type_: List of <a href="coordinatesdefinition.md">CoordinatesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ElinNumber

_Required_: No

_Type_: List of <a href="elinnumberdefinition.md">ElinNumberDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

