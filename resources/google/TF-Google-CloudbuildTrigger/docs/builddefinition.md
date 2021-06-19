# TF::Google::CloudbuildTrigger BuildDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#images" title="Images">Images</a>" : <i>[ String, ... ]</i>,
    "<a href="#logsbucket" title="LogsBucket">LogsBucket</a>" : <i>String</i>,
    "<a href="#queuettl" title="QueueTtl">QueueTtl</a>" : <i>String</i>,
    "<a href="#substitutions" title="Substitutions">Substitutions</a>" : <i>[ <a href="substitutionsdefinition.md">SubstitutionsDefinition</a>, ... ]</i>,
    "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
    "<a href="#timeout" title="Timeout">Timeout</a>" : <i>String</i>,
    "<a href="#artifacts" title="Artifacts">Artifacts</a>" : <i>[ <a href="artifactsdefinition.md">ArtifactsDefinition</a>, ... ]</i>,
    "<a href="#options" title="Options">Options</a>" : <i>[ <a href="optionsdefinition.md">OptionsDefinition</a>, ... ]</i>,
    "<a href="#secret" title="Secret">Secret</a>" : <i>[ <a href="secretdefinition.md">SecretDefinition</a>, ... ]</i>,
    "<a href="#source" title="Source">Source</a>" : <i>[ <a href="sourcedefinition.md">SourceDefinition</a>, ... ]</i>,
    "<a href="#step" title="Step">Step</a>" : <i>[ <a href="stepdefinition.md">StepDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#images" title="Images">Images</a>: <i>
      - String</i>
<a href="#logsbucket" title="LogsBucket">LogsBucket</a>: <i>String</i>
<a href="#queuettl" title="QueueTtl">QueueTtl</a>: <i>String</i>
<a href="#substitutions" title="Substitutions">Substitutions</a>: <i>
      - <a href="substitutionsdefinition.md">SubstitutionsDefinition</a></i>
<a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
<a href="#timeout" title="Timeout">Timeout</a>: <i>String</i>
<a href="#artifacts" title="Artifacts">Artifacts</a>: <i>
      - <a href="artifactsdefinition.md">ArtifactsDefinition</a></i>
<a href="#options" title="Options">Options</a>: <i>
      - <a href="optionsdefinition.md">OptionsDefinition</a></i>
<a href="#secret" title="Secret">Secret</a>: <i>
      - <a href="secretdefinition.md">SecretDefinition</a></i>
<a href="#source" title="Source">Source</a>: <i>
      - <a href="sourcedefinition.md">SourceDefinition</a></i>
<a href="#step" title="Step">Step</a>: <i>
      - <a href="stepdefinition.md">StepDefinition</a></i>
</pre>

## Properties

#### Images

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogsBucket

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueueTtl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Substitutions

_Required_: No

_Type_: List of <a href="substitutionsdefinition.md">SubstitutionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeout

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Artifacts

_Required_: No

_Type_: List of <a href="artifactsdefinition.md">ArtifactsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Options

_Required_: No

_Type_: List of <a href="optionsdefinition.md">OptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Secret

_Required_: No

_Type_: List of <a href="secretdefinition.md">SecretDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

_Required_: No

_Type_: List of <a href="sourcedefinition.md">SourceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Step

_Required_: No

_Type_: List of <a href="stepdefinition.md">StepDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

