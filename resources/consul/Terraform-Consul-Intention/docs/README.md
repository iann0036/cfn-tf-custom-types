# Terraform::Consul::Intention

[Intentions](https://www.consul.io/docs/connect/intentions.html) are used to define
rules for which services may connect to one another when using [Consul Connect](https://www.consul.io/docs/connect/index.html).

It is appropriate to either reference existing services or specify non-existent services
that will be created in the future when creating intentions. This resource can be used
in conjunction with the `consul_service` datasource when referencing services
registered on nodes that have a running Consul agent.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Consul::Intention",
    "Properties" : {
        "<a href="#action" title="Action">Action</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#destinationname" title="DestinationName">DestinationName</a>" : <i>String</i>,
        "<a href="#meta" title="Meta">Meta</a>" : <i>[ <a href="meta.md">Meta</a>, ... ]</i>,
        "<a href="#sourcename" title="SourceName">SourceName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Consul::Intention
Properties:
    <a href="#action" title="Action">Action</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#destinationname" title="DestinationName">DestinationName</a>: <i>String</i>
    <a href="#meta" title="Meta">Meta</a>: <i>
      - <a href="meta.md">Meta</a></i>
    <a href="#sourcename" title="SourceName">SourceName</a>: <i>String</i>
</pre>

## Properties

#### Action

The intention action. Must be one of `allow` or `deny`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Optional description that can be used by Consul
tooling, but is not used internally.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationName

The name of the destination service for the intention. This
service does not have to exist.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Meta

Key/value pairs that are opaque to Consul and are associated
with the intention.

_Required_: No

_Type_: List of <a href="meta.md">Meta</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceName

The name of the source service for the intention. This
service does not have to exist.

_Required_: Yes

_Type_: String

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

