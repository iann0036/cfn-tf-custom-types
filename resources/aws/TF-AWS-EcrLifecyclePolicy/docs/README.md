# TF::AWS::EcrLifecyclePolicy

Manages an ECR repository lifecycle policy.

~> **NOTE:** Only one `aws_ecr_lifecycle_policy` resource can be used with the same ECR repository. To apply multiple rules, they must be combined in the `policy` JSON.

~> **NOTE:** The AWS ECR API seems to reorder rules based on `rulePriority`. If you define multiple rules that are not sorted in ascending `rulePriority` order in the Terraform code, the resource will be flagged for recreation every `terraform plan`.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::EcrLifecyclePolicy",
    "Properties" : {
        "<a href="#policy" title="Policy">Policy</a>" : <i>String</i>,
        "<a href="#repository" title="Repository">Repository</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::EcrLifecyclePolicy
Properties:
    <a href="#policy" title="Policy">Policy</a>: <i>String</i>
    <a href="#repository" title="Repository">Repository</a>: <i>String</i>
</pre>

## Properties

#### Policy

The policy document. This is a JSON formatted string. See more details about [Policy Parameters](http://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html#lifecycle_policy_parameters) in the official AWS docs. For more information about building IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](https://learn.hashicorp.com/terraform/aws/iam-policy).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Repository

Name of the repository to apply the policy.

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

#### RegistryId

Returns the <code>RegistryId</code> value.

