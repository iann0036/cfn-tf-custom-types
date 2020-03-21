# Terraform::OCI::DatascienceModelProvenance

CloudFormation equivalent of oci_datascience_model_provenance

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OCI::DatascienceModelProvenance",
    "Properties" : {
        "<a href="#gitbranch" title="GitBranch">GitBranch</a>" : <i>String</i>,
        "<a href="#gitcommit" title="GitCommit">GitCommit</a>" : <i>String</i>,
        "<a href="#modelid" title="ModelId">ModelId</a>" : <i>String</i>,
        "<a href="#repositoryurl" title="RepositoryUrl">RepositoryUrl</a>" : <i>String</i>,
        "<a href="#scriptdir" title="ScriptDir">ScriptDir</a>" : <i>String</i>,
        "<a href="#trainingscript" title="TrainingScript">TrainingScript</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OCI::DatascienceModelProvenance
Properties:
    <a href="#gitbranch" title="GitBranch">GitBranch</a>: <i>String</i>
    <a href="#gitcommit" title="GitCommit">GitCommit</a>: <i>String</i>
    <a href="#modelid" title="ModelId">ModelId</a>: <i>String</i>
    <a href="#repositoryurl" title="RepositoryUrl">RepositoryUrl</a>: <i>String</i>
    <a href="#scriptdir" title="ScriptDir">ScriptDir</a>: <i>String</i>
    <a href="#trainingscript" title="TrainingScript">TrainingScript</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### GitBranch

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GitCommit

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ModelId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RepositoryUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScriptDir

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrainingScript

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

