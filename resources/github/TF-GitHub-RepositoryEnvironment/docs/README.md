# TF::GitHub::RepositoryEnvironment

CloudFormation equivalent of github_repository_environment

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::GitHub::RepositoryEnvironment",
    "Properties" : {
        "<a href="#environment" title="Environment">Environment</a>" : <i>String</i>,
        "<a href="#repository" title="Repository">Repository</a>" : <i>String</i>,
        "<a href="#waittimer" title="WaitTimer">WaitTimer</a>" : <i>Double</i>,
        "<a href="#deploymentbranchpolicy" title="DeploymentBranchPolicy">DeploymentBranchPolicy</a>" : <i>[ <a href="deploymentbranchpolicydefinition.md">DeploymentBranchPolicyDefinition</a>, ... ]</i>,
        "<a href="#reviewers" title="Reviewers">Reviewers</a>" : <i>[ <a href="reviewersdefinition.md">ReviewersDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::GitHub::RepositoryEnvironment
Properties:
    <a href="#environment" title="Environment">Environment</a>: <i>String</i>
    <a href="#repository" title="Repository">Repository</a>: <i>String</i>
    <a href="#waittimer" title="WaitTimer">WaitTimer</a>: <i>Double</i>
    <a href="#deploymentbranchpolicy" title="DeploymentBranchPolicy">DeploymentBranchPolicy</a>: <i>
      - <a href="deploymentbranchpolicydefinition.md">DeploymentBranchPolicyDefinition</a></i>
    <a href="#reviewers" title="Reviewers">Reviewers</a>: <i>
      - <a href="reviewersdefinition.md">ReviewersDefinition</a></i>
</pre>

## Properties

#### Environment

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Repository

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaitTimer

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeploymentBranchPolicy

_Required_: No

_Type_: List of <a href="deploymentbranchpolicydefinition.md">DeploymentBranchPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Reviewers

_Required_: No

_Type_: List of <a href="reviewersdefinition.md">ReviewersDefinition</a>

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

