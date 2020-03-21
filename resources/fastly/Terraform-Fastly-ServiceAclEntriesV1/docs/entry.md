# Terraform::Fastly::ServiceAclEntriesV1 Entry

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
    "<a href="#ip" title="Ip">Ip</a>" : <i>String</i>,
    "<a href="#negated" title="Negated">Negated</a>" : <i>Boolean</i>,
    "<a href="#subnet" title="Subnet">Subnet</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#comment" title="Comment">Comment</a>: <i>String</i>
<a href="#ip" title="Ip">Ip</a>: <i>String</i>
<a href="#negated" title="Negated">Negated</a>: <i>Boolean</i>
<a href="#subnet" title="Subnet">Subnet</a>: <i>String</i>
</pre>

## Properties

#### Comment

A personal freeform descriptive note.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip

An IP address that is the focus for the ACL.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Negated

A boolean that will negate the match if true.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnet

An optional subnet mask applied to the IP address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

