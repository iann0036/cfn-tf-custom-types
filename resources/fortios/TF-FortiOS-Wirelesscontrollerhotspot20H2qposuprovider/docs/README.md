# TF::FortiOS::Wirelesscontrollerhotspot20H2qposuprovider

Configure online sign up (OSU) provider list.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::Wirelesscontrollerhotspot20H2qposuprovider",
    "Properties" : {
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#icon" title="Icon">Icon</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#osumethod" title="OsuMethod">OsuMethod</a>" : <i>String</i>,
        "<a href="#osunai" title="OsuNai">OsuNai</a>" : <i>String</i>,
        "<a href="#serveruri" title="ServerUri">ServerUri</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#friendlyname" title="FriendlyName">FriendlyName</a>" : <i>[ <a href="friendlynamedefinition.md">FriendlyNameDefinition</a>, ... ]</i>,
        "<a href="#servicedescription" title="ServiceDescription">ServiceDescription</a>" : <i>[ <a href="servicedescriptiondefinition.md">ServiceDescriptionDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::Wirelesscontrollerhotspot20H2qposuprovider
Properties:
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#icon" title="Icon">Icon</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#osumethod" title="OsuMethod">OsuMethod</a>: <i>String</i>
    <a href="#osunai" title="OsuNai">OsuNai</a>: <i>String</i>
    <a href="#serveruri" title="ServerUri">ServerUri</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#friendlyname" title="FriendlyName">FriendlyName</a>: <i>
      - <a href="friendlynamedefinition.md">FriendlyNameDefinition</a></i>
    <a href="#servicedescription" title="ServiceDescription">ServiceDescription</a>: <i>
      - <a href="servicedescriptiondefinition.md">ServiceDescriptionDefinition</a></i>
</pre>

## Properties

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Icon

OSU provider icon.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

OSU provider ID.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsuMethod

OSU method list. Valid values: `oma-dm`, `soap-xml-spp`, `reserved`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsuNai

OSU NAI.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerUri

Server URI.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FriendlyName

_Required_: No

_Type_: List of <a href="friendlynamedefinition.md">FriendlyNameDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceDescription

_Required_: No

_Type_: List of <a href="servicedescriptiondefinition.md">ServiceDescriptionDefinition</a>

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

