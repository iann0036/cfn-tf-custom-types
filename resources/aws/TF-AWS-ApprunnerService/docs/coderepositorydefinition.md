# TF::AWS::ApprunnerService CodeRepositoryDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#repositoryurl" title="RepositoryUrl">RepositoryUrl</a>" : <i>String</i>,
    "<a href="#codeconfiguration" title="CodeConfiguration">CodeConfiguration</a>" : <i>[ <a href="codeconfigurationdefinition.md">CodeConfigurationDefinition</a>, ... ]</i>,
    "<a href="#sourcecodeversion" title="SourceCodeVersion">SourceCodeVersion</a>" : <i>[ <a href="sourcecodeversiondefinition.md">SourceCodeVersionDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#repositoryurl" title="RepositoryUrl">RepositoryUrl</a>: <i>String</i>
<a href="#codeconfiguration" title="CodeConfiguration">CodeConfiguration</a>: <i>
      - <a href="codeconfigurationdefinition.md">CodeConfigurationDefinition</a></i>
<a href="#sourcecodeversion" title="SourceCodeVersion">SourceCodeVersion</a>: <i>
      - <a href="sourcecodeversiondefinition.md">SourceCodeVersionDefinition</a></i>
</pre>

## Properties

#### RepositoryUrl

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CodeConfiguration

_Required_: No

_Type_: List of <a href="codeconfigurationdefinition.md">CodeConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceCodeVersion

_Required_: No

_Type_: List of <a href="sourcecodeversiondefinition.md">SourceCodeVersionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

