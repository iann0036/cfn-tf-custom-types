# TF::OCI::DatabaseAutonomousContainerDatabase BackupConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#recoverywindowindays" title="RecoveryWindowInDays">RecoveryWindowInDays</a>" : <i>Double</i>,
    "<a href="#backupdestinationdetails" title="BackupDestinationDetails">BackupDestinationDetails</a>" : <i>[ <a href="backupdestinationdetailsdefinition.md">BackupDestinationDetailsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#recoverywindowindays" title="RecoveryWindowInDays">RecoveryWindowInDays</a>: <i>Double</i>
<a href="#backupdestinationdetails" title="BackupDestinationDetails">BackupDestinationDetails</a>: <i>
      - <a href="backupdestinationdetailsdefinition.md">BackupDestinationDetailsDefinition</a></i>
</pre>

## Properties

#### RecoveryWindowInDays

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupDestinationDetails

_Required_: No

_Type_: List of <a href="backupdestinationdetailsdefinition.md">BackupDestinationDetailsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

