# TF::OCI::DatascienceNotebookSession NotebookSessionConfigurationDetailsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#blockstoragesizeingbs" title="BlockStorageSizeInGbs">BlockStorageSizeInGbs</a>" : <i>Double</i>,
    "<a href="#shape" title="Shape">Shape</a>" : <i>String</i>,
    "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>,
    "<a href="#notebooksessionshapeconfigdetails" title="NotebookSessionShapeConfigDetails">NotebookSessionShapeConfigDetails</a>" : <i>[ <a href="notebooksessionshapeconfigdetailsdefinition.md">NotebookSessionShapeConfigDetailsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#blockstoragesizeingbs" title="BlockStorageSizeInGbs">BlockStorageSizeInGbs</a>: <i>Double</i>
<a href="#shape" title="Shape">Shape</a>: <i>String</i>
<a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
<a href="#notebooksessionshapeconfigdetails" title="NotebookSessionShapeConfigDetails">NotebookSessionShapeConfigDetails</a>: <i>
      - <a href="notebooksessionshapeconfigdetailsdefinition.md">NotebookSessionShapeConfigDetailsDefinition</a></i>
</pre>

## Properties

#### BlockStorageSizeInGbs

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Shape

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotebookSessionShapeConfigDetails

_Required_: No

_Type_: List of <a href="notebooksessionshapeconfigdetailsdefinition.md">NotebookSessionShapeConfigDetailsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

