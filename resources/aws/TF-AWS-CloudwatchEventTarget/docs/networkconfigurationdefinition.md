# TF::AWS::CloudwatchEventTarget NetworkConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#assignpublicip" title="AssignPublicIp">AssignPublicIp</a>" : <i>Boolean</i>,
    "<a href="#securitygroups" title="SecurityGroups">SecurityGroups</a>" : <i>[ String, ... ]</i>,
    "<a href="#subnets" title="Subnets">Subnets</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#assignpublicip" title="AssignPublicIp">AssignPublicIp</a>: <i>Boolean</i>
<a href="#securitygroups" title="SecurityGroups">SecurityGroups</a>: <i>
      - String</i>
<a href="#subnets" title="Subnets">Subnets</a>: <i>
      - String</i>
</pre>

## Properties

#### AssignPublicIp

Assign a public IP address to the ENI (Fargate launch type only). Valid values are `true` or `false`. Default `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroups

The security groups associated with the task or service. If you do not specify a security group, the default security group for the VPC is used.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnets

The subnets associated with the task or service.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

