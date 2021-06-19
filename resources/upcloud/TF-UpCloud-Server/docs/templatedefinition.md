# TF::UpCloud::Server TemplateDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#address" title="Address">Address</a>" : <i>String</i>,
    "<a href="#size" title="Size">Size</a>" : <i>Double</i>,
    "<a href="#storage" title="Storage">Storage</a>" : <i>String</i>,
    "<a href="#title" title="Title">Title</a>" : <i>String</i>,
    "<a href="#backuprule" title="BackupRule">BackupRule</a>" : <i>[ <a href="backupruledefinition.md">BackupRuleDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#address" title="Address">Address</a>: <i>String</i>
<a href="#size" title="Size">Size</a>: <i>Double</i>
<a href="#storage" title="Storage">Storage</a>: <i>String</i>
<a href="#title" title="Title">Title</a>: <i>String</i>
<a href="#backuprule" title="BackupRule">BackupRule</a>: <i>
      - <a href="backupruledefinition.md">BackupRuleDefinition</a></i>
</pre>

## Properties

#### Address

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Size

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Storage

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Title

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupRule

_Required_: No

_Type_: List of <a href="backupruledefinition.md">BackupRuleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

