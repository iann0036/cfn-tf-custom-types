# TF::AWS::AutoscalingAttachment

Provides an Auto Scaling Attachment resource.

~> **NOTE on Auto Scaling Groups and ASG Attachments:** Terraform currently provides
both a standalone [`aws_autoscaling_attachment`](autoscaling_attachment.html) resource
(describing an ASG attached to an ELB or ALB), and an [`aws_autoscaling_group`](autoscaling_group.html)
with `load_balancers` and `target_group_arns` defined in-line. These two methods are not
mutually-exclusive. If `aws_autoscaling_attachment` resources are used, either alone or with inline
`load_balancers` or `target_group_arns`, the `aws_autoscaling_group` resource must be configured
to ignore changes to the `load_balancers` and `target_group_arns` arguments within a
[`lifecycle` configuration block](https://www.terraform.io/docs/configuration/meta-arguments/lifecycle.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::AutoscalingAttachment",
    "Properties" : {
        "<a href="#albtargetgrouparn" title="AlbTargetGroupArn">AlbTargetGroupArn</a>" : <i>String</i>,
        "<a href="#autoscalinggroupname" title="AutoscalingGroupName">AutoscalingGroupName</a>" : <i>String</i>,
        "<a href="#elb" title="Elb">Elb</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::AutoscalingAttachment
Properties:
    <a href="#albtargetgrouparn" title="AlbTargetGroupArn">AlbTargetGroupArn</a>: <i>String</i>
    <a href="#autoscalinggroupname" title="AutoscalingGroupName">AutoscalingGroupName</a>: <i>String</i>
    <a href="#elb" title="Elb">Elb</a>: <i>String</i>
</pre>

## Properties

#### AlbTargetGroupArn

The ARN of an ALB Target Group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscalingGroupName

Name of ASG to associate with the ELB.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Elb

The name of the ELB.

_Required_: No

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

