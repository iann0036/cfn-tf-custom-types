# TF::Equinix::NetworkAclTemplate

Resource `equinix_network_acl_template` allows creation and management of
Equinix Network Edge device Access Control List templates.

Device ACL templates give possibility to define set of rules will allowed inbound
traffic. Templates can be assigned to the network devices.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Equinix::NetworkAclTemplate",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#metrocode" title="MetroCode">MetroCode</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#inboundrule" title="InboundRule">InboundRule</a>" : <i>[ <a href="inboundruledefinition.md">InboundRuleDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Equinix::NetworkAclTemplate
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#metrocode" title="MetroCode">MetroCode</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#inboundrule" title="InboundRule">InboundRule</a>: <i>
      - <a href="inboundruledefinition.md">InboundRuleDefinition</a></i>
</pre>

## Properties

#### Description

ACL template description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetroCode

ACL template location metro code.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

ACL template name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InboundRule

_Required_: No

_Type_: List of <a href="inboundruledefinition.md">InboundRuleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### DeviceAclStatus

Returns the <code>DeviceAclStatus</code> value.

#### DeviceId

Returns the <code>DeviceId</code> value.

#### Id

Returns the <code>Id</code> value.

#### Uuid

Returns the <code>Uuid</code> value.

