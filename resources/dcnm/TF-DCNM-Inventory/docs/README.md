# TF::DCNM::Inventory

CloudFormation equivalent of dcnm_inventory

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::DCNM::Inventory",
    "Properties" : {
        "<a href="#authprotocol" title="AuthProtocol">AuthProtocol</a>" : <i>Double</i>,
        "<a href="#configtimeout" title="ConfigTimeout">ConfigTimeout</a>" : <i>Double</i>,
        "<a href="#deploy" title="Deploy">Deploy</a>" : <i>Boolean</i>,
        "<a href="#fabricname" title="FabricName">FabricName</a>" : <i>String</i>,
        "<a href="#ips" title="Ips">Ips</a>" : <i>[ String, ... ]</i>,
        "<a href="#maxhops" title="MaxHops">MaxHops</a>" : <i>Double</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#platform" title="Platform">Platform</a>" : <i>String</i>,
        "<a href="#preserveconfig" title="PreserveConfig">PreserveConfig</a>" : <i>String</i>,
        "<a href="#secondtimeout" title="SecondTimeout">SecondTimeout</a>" : <i>Double</i>,
        "<a href="#username" title="Username">Username</a>" : <i>String</i>,
        "<a href="#switchconfig" title="SwitchConfig">SwitchConfig</a>" : <i>[ <a href="switchconfigdefinition.md">SwitchConfigDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::DCNM::Inventory
Properties:
    <a href="#authprotocol" title="AuthProtocol">AuthProtocol</a>: <i>Double</i>
    <a href="#configtimeout" title="ConfigTimeout">ConfigTimeout</a>: <i>Double</i>
    <a href="#deploy" title="Deploy">Deploy</a>: <i>Boolean</i>
    <a href="#fabricname" title="FabricName">FabricName</a>: <i>String</i>
    <a href="#ips" title="Ips">Ips</a>: <i>
      - String</i>
    <a href="#maxhops" title="MaxHops">MaxHops</a>: <i>Double</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#platform" title="Platform">Platform</a>: <i>String</i>
    <a href="#preserveconfig" title="PreserveConfig">PreserveConfig</a>: <i>String</i>
    <a href="#secondtimeout" title="SecondTimeout">SecondTimeout</a>: <i>Double</i>
    <a href="#username" title="Username">Username</a>: <i>String</i>
    <a href="#switchconfig" title="SwitchConfig">SwitchConfig</a>: <i>
      - <a href="switchconfigdefinition.md">SwitchConfigDefinition</a></i>
</pre>

## Properties

#### AuthProtocol

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Deploy

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FabricName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ips

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxHops

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Platform

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreserveConfig

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecondTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Username

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SwitchConfig

_Required_: No

_Type_: List of <a href="switchconfigdefinition.md">SwitchConfigDefinition</a>

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

