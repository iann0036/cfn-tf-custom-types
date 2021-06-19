# TF::B2::Bucket FileLockConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#isfilelockenabled" title="IsFileLockEnabled">IsFileLockEnabled</a>" : <i>Boolean</i>,
    "<a href="#defaultretention" title="DefaultRetention">DefaultRetention</a>" : <i>[ <a href="defaultretentiondefinition.md">DefaultRetentionDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#isfilelockenabled" title="IsFileLockEnabled">IsFileLockEnabled</a>: <i>Boolean</i>
<a href="#defaultretention" title="DefaultRetention">DefaultRetention</a>: <i>
      - <a href="defaultretentiondefinition.md">DefaultRetentionDefinition</a></i>
</pre>

## Properties

#### IsFileLockEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultRetention

_Required_: No

_Type_: List of <a href="defaultretentiondefinition.md">DefaultRetentionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

