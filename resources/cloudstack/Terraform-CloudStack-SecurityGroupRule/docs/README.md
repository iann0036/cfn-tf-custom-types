# Terraform::CloudStack::SecurityGroupRule

Authorizes and revokes both ingress and egress rulea for a given security group.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::CloudStack::SecurityGroupRule",
    "Properties" : {
        "<a href="#parallelism" title="Parallelism">Parallelism</a>" : <i>Double</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#securitygroupid" title="SecurityGroupId">SecurityGroupId</a>" : <i>String</i>,
        "<a href="#rule" title="Rule">Rule</a>" : <i>[ <a href="rule.md">Rule</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::CloudStack::SecurityGroupRule
Properties:
    <a href="#parallelism" title="Parallelism">Parallelism</a>: <i>Double</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#securitygroupid" title="SecurityGroupId">SecurityGroupId</a>: <i>String</i>
    <a href="#rule" title="Rule">Rule</a>: <i>
      - <a href="rule.md">Rule</a></i>
</pre>

## Properties

#### Parallelism

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

The name or ID of the project in which the security
group is created. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroupId

The security group ID for which to create
the rules. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rule

_Required_: No

_Type_: List of <a href="rule.md">Rule</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

