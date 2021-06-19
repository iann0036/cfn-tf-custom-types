# TF::RedisCloud::Subscription AllowlistDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cidrs" title="Cidrs">Cidrs</a>" : <i>[ String, ... ]</i>,
    "<a href="#securitygroupids" title="SecurityGroupIds">SecurityGroupIds</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#cidrs" title="Cidrs">Cidrs</a>: <i>
      - String</i>
<a href="#securitygroupids" title="SecurityGroupIds">SecurityGroupIds</a>: <i>
      - String</i>
</pre>

## Properties

#### Cidrs

Set of CIDR ranges that are allowed to access the databases associated with this subscription.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroupIds

Set of security groups that are allowed to access the databases associated with this subscription.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

