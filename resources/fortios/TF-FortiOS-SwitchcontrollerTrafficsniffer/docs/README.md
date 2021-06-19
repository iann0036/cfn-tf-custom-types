# TF::FortiOS::SwitchcontrollerTrafficsniffer

Configure FortiSwitch RSPAN/ERSPAN traffic sniffing parameters.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::SwitchcontrollerTrafficsniffer",
    "Properties" : {
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#erspanip" title="ErspanIp">ErspanIp</a>" : <i>String</i>,
        "<a href="#mode" title="Mode">Mode</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#targetip" title="TargetIp">TargetIp</a>" : <i>[ <a href="targetipdefinition.md">TargetIpDefinition</a>, ... ]</i>,
        "<a href="#targetmac" title="TargetMac">TargetMac</a>" : <i>[ <a href="targetmacdefinition.md">TargetMacDefinition</a>, ... ]</i>,
        "<a href="#targetport" title="TargetPort">TargetPort</a>" : <i>[ <a href="targetportdefinition.md">TargetPortDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::SwitchcontrollerTrafficsniffer
Properties:
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#erspanip" title="ErspanIp">ErspanIp</a>: <i>String</i>
    <a href="#mode" title="Mode">Mode</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#targetip" title="TargetIp">TargetIp</a>: <i>
      - <a href="targetipdefinition.md">TargetIpDefinition</a></i>
    <a href="#targetmac" title="TargetMac">TargetMac</a>: <i>
      - <a href="targetmacdefinition.md">TargetMacDefinition</a></i>
    <a href="#targetport" title="TargetPort">TargetPort</a>: <i>
      - <a href="targetportdefinition.md">TargetPortDefinition</a></i>
</pre>

## Properties

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ErspanIp

Configure ERSPAN collector IP address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mode

Configure traffic sniffer mode. Valid values: `erspan-auto`, `rspan`, `none`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetIp

_Required_: No

_Type_: List of <a href="targetipdefinition.md">TargetIpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetMac

_Required_: No

_Type_: List of <a href="targetmacdefinition.md">TargetMacDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetPort

_Required_: No

_Type_: List of <a href="targetportdefinition.md">TargetPortDefinition</a>

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

