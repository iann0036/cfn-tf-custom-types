# TF::AWS::Kinesisanalyticsv2Application ApplicationRestoreConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#applicationrestoretype" title="ApplicationRestoreType">ApplicationRestoreType</a>" : <i>String</i>,
    "<a href="#snapshotname" title="SnapshotName">SnapshotName</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#applicationrestoretype" title="ApplicationRestoreType">ApplicationRestoreType</a>: <i>String</i>
<a href="#snapshotname" title="SnapshotName">SnapshotName</a>: <i>String</i>
</pre>

## Properties

#### ApplicationRestoreType

Specifies how the application should be restored. Valid values: `RESTORE_FROM_CUSTOM_SNAPSHOT`, `RESTORE_FROM_LATEST_SNAPSHOT`, `SKIP_RESTORE_FROM_SNAPSHOT`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnapshotName

The identifier of an existing snapshot of application state to use to restart an application. The application uses this value if `RESTORE_FROM_CUSTOM_SNAPSHOT` is specified for `application_restore_type`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

