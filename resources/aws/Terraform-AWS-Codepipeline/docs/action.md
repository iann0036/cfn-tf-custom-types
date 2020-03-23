# Terraform::AWS::Codepipeline Action

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#category" title="Category">Category</a>" : <i>String</i>,
    "<a href="#configuration" title="Configuration">Configuration</a>" : <i>[ <a href="action-configuration.md">Configuration</a>, ... ]</i>,
    "<a href="#inputartifacts" title="InputArtifacts">InputArtifacts</a>" : <i>[ String, ... ]</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#outputartifacts" title="OutputArtifacts">OutputArtifacts</a>" : <i>[ String, ... ]</i>,
    "<a href="#owner" title="Owner">Owner</a>" : <i>String</i>,
    "<a href="#provider" title="Provider">Provider</a>" : <i>String</i>,
    "<a href="#rolearn" title="RoleArn">RoleArn</a>" : <i>String</i>,
    "<a href="#runorder" title="RunOrder">RunOrder</a>" : <i>Double</i>,
    "<a href="#version" title="Version">Version</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#category" title="Category">Category</a>: <i>String</i>
<a href="#configuration" title="Configuration">Configuration</a>: <i>
      - <a href="action-configuration.md">Configuration</a></i>
<a href="#inputartifacts" title="InputArtifacts">InputArtifacts</a>: <i>
      - String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#outputartifacts" title="OutputArtifacts">OutputArtifacts</a>: <i>
      - String</i>
<a href="#owner" title="Owner">Owner</a>: <i>String</i>
<a href="#provider" title="Provider">Provider</a>: <i>String</i>
<a href="#rolearn" title="RoleArn">RoleArn</a>: <i>String</i>
<a href="#runorder" title="RunOrder">RunOrder</a>: <i>Double</i>
<a href="#version" title="Version">Version</a>: <i>String</i>
</pre>

## Properties

#### Category

A category defines what kind of action can be taken in the stage, and constrains the provider type for the action. Possible values are `Approval`, `Build`, `Deploy`, `Invoke`, `Source` and `Test`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Configuration

A Map of the action declaration's configuration. Find out more about configuring action configurations in the [Reference Pipeline Structure documentation](http://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#action-requirements).

_Required_: No

_Type_: List of <a href="action-configuration.md">Configuration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InputArtifacts

A list of artifact names to be worked on.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The action declaration's name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutputArtifacts

A list of artifact names to output. Output artifact names must be unique within a pipeline.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Owner

The creator of the action being called. Possible values are `AWS`, `Custom` and `ThirdParty`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Provider

The provider of the service being called by the action. Valid providers are determined by the action category. For example, an action in the Deploy category type might have a provider of AWS CodeDeploy, which would be specified as CodeDeploy.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleArn

The ARN of the IAM service role that will perform the declared action. This is assumed through the roleArn for the pipeline.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RunOrder

The order in which actions are run.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

A string that identifies the action type.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

