# Terraform::AWS::ElbAttachment

Attaches an EC2 instance to an Elastic Load Balancer (ELB). For attaching resources with Application Load Balancer (ALB) or Network Load Balancer (NLB), see the [`aws_lb_target_group_attachment` resource](/docs/providers/aws/r/lb_target_group_attachment.html).

~> **NOTE on ELB Instances and ELB Attachments:** Terraform currently provides
both a standalone ELB Attachment resource (describing an instance attached to
an ELB), and an [Elastic Load Balancer resource](elb.html) with
`instances` defined in-line. At this time you cannot use an ELB with in-line
instances in conjunction with an ELB Attachment resource. Doing so will cause a
conflict and will overwrite attachments.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::ElbAttachment",
    "Properties" : {
        "<a href="#elb" title="Elb">Elb</a>" : <i>String</i>,
        "<a href="#instance" title="Instance">Instance</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::ElbAttachment
Properties:
    <a href="#elb" title="Elb">Elb</a>: <i>String</i>
    <a href="#instance" title="Instance">Instance</a>: <i>String</i>
</pre>

## Properties

#### Elb

The name of the ELB.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Instance

Instance ID to place in the ELB pool.

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

