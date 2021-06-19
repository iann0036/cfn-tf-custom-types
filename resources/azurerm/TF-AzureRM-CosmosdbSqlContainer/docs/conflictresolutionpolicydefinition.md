# TF::AzureRM::CosmosdbSqlContainer ConflictResolutionPolicyDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#conflictresolutionpath" title="ConflictResolutionPath">ConflictResolutionPath</a>" : <i>String</i>,
    "<a href="#conflictresolutionprocedure" title="ConflictResolutionProcedure">ConflictResolutionProcedure</a>" : <i>String</i>,
    "<a href="#mode" title="Mode">Mode</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#conflictresolutionpath" title="ConflictResolutionPath">ConflictResolutionPath</a>: <i>String</i>
<a href="#conflictresolutionprocedure" title="ConflictResolutionProcedure">ConflictResolutionProcedure</a>: <i>String</i>
<a href="#mode" title="Mode">Mode</a>: <i>String</i>
</pre>

## Properties

#### ConflictResolutionPath

The conflict resolution path in the case of `LastWriterWins` mode.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConflictResolutionProcedure

The procedure to resolve conflicts in the case of `Custom` mode.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mode

Indicates the conflict resolution mode. Possible values include: `LastWriterWins`, `Custom`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

