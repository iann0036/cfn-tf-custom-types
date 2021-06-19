# TF::DME::VanityNameserverRecord

CloudFormation equivalent of dme_vanity_nameserver_record

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::DME::VanityNameserverRecord",
    "Properties" : {
        "<a href="#defaultconfig" title="DefaultConfig">DefaultConfig</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nameservergroupid" title="NameServerGroupId">NameServerGroupId</a>" : <i>Double</i>,
        "<a href="#publicconfig" title="PublicConfig">PublicConfig</a>" : <i>Boolean</i>,
        "<a href="#servers" title="Servers">Servers</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::DME::VanityNameserverRecord
Properties:
    <a href="#defaultconfig" title="DefaultConfig">DefaultConfig</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nameservergroupid" title="NameServerGroupId">NameServerGroupId</a>: <i>Double</i>
    <a href="#publicconfig" title="PublicConfig">PublicConfig</a>: <i>Boolean</i>
    <a href="#servers" title="Servers">Servers</a>: <i>
      - String</i>
</pre>

## Properties

#### DefaultConfig

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NameServerGroupId

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicConfig

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Servers

_Required_: Yes

_Type_: List of String

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

