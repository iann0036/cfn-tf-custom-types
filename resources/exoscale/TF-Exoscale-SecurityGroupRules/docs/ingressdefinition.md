# TF::Exoscale::SecurityGroupRules IngressDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cidrlist" title="CidrList">CidrList</a>" : <i>[ String, ... ]</i>,
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#icmpcode" title="IcmpCode">IcmpCode</a>" : <i>Double</i>,
    "<a href="#icmptype" title="IcmpType">IcmpType</a>" : <i>Double</i>,
    "<a href="#ports" title="Ports">Ports</a>" : <i>[ String, ... ]</i>,
    "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
    "<a href="#usersecuritygrouplist" title="UserSecurityGroupList">UserSecurityGroupList</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#cidrlist" title="CidrList">CidrList</a>: <i>
      - String</i>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#icmpcode" title="IcmpCode">IcmpCode</a>: <i>Double</i>
<a href="#icmptype" title="IcmpType">IcmpType</a>: <i>Double</i>
<a href="#ports" title="Ports">Ports</a>: <i>
      - String</i>
<a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
<a href="#usersecuritygrouplist" title="UserSecurityGroupList">UserSecurityGroupList</a>: <i>
      - String</i>
</pre>

## Properties

#### CidrList

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IcmpCode

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IcmpType

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ports

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserSecurityGroupList

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

