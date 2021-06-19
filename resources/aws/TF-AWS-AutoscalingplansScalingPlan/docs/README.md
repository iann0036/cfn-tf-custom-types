# TF::AWS::AutoscalingplansScalingPlan

Manages an AWS Auto Scaling scaling plan.
More information can be found in the [AWS Auto Scaling User Guide](https://docs.aws.amazon.com/autoscaling/plans/userguide/what-is-aws-auto-scaling.html).

~> **NOTE:** The AWS Auto Scaling service uses an AWS IAM service-linked role to manage predictive scaling of Amazon EC2 Auto Scaling groups. The service attempts to automatically create this role the first time a scaling plan with predictive scaling enabled is created.
An [`aws_iam_service_linked_role`](/docs/providers/aws/r/iam_service_linked_role.html) resource can be used to manually manage this role.
See the [AWS documentation](https://docs.aws.amazon.com/autoscaling/plans/userguide/aws-auto-scaling-service-linked-roles.html#create-service-linked-role-manual) for more details.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::AutoscalingplansScalingPlan",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#applicationsource" title="ApplicationSource">ApplicationSource</a>" : <i>[ <a href="applicationsourcedefinition.md">ApplicationSourceDefinition</a>, ... ]</i>,
        "<a href="#scalinginstruction" title="ScalingInstruction">ScalingInstruction</a>" : <i>[ <a href="scalinginstructiondefinition.md">ScalingInstructionDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::AutoscalingplansScalingPlan
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#applicationsource" title="ApplicationSource">ApplicationSource</a>: <i>
      - <a href="applicationsourcedefinition.md">ApplicationSourceDefinition</a></i>
    <a href="#scalinginstruction" title="ScalingInstruction">ScalingInstruction</a>: <i>
      - <a href="scalinginstructiondefinition.md">ScalingInstructionDefinition</a></i>
</pre>

## Properties

#### Name

The name of the scaling plan. Names cannot contain vertical bars, colons, or forward slashes.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplicationSource

_Required_: No

_Type_: List of <a href="applicationsourcedefinition.md">ApplicationSourceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScalingInstruction

_Required_: No

_Type_: List of <a href="scalinginstructiondefinition.md">ScalingInstructionDefinition</a>

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

#### ScalingPlanVersion

Returns the <code>ScalingPlanVersion</code> value.

