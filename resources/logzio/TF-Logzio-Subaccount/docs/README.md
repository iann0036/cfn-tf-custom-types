# TF::Logzio::Subaccount

CloudFormation equivalent of logzio_subaccount

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Logzio::Subaccount",
    "Properties" : {
        "<a href="#accessible" title="Accessible">Accessible</a>" : <i>Boolean</i>,
        "<a href="#accountname" title="AccountName">AccountName</a>" : <i>String</i>,
        "<a href="#docsizesetting" title="DocSizeSetting">DocSizeSetting</a>" : <i>Boolean</i>,
        "<a href="#email" title="Email">Email</a>" : <i>String</i>,
        "<a href="#maxdailygb" title="MaxDailyGb">MaxDailyGb</a>" : <i>Double</i>,
        "<a href="#retentiondays" title="RetentionDays">RetentionDays</a>" : <i>Double</i>,
        "<a href="#searchable" title="Searchable">Searchable</a>" : <i>Boolean</i>,
        "<a href="#sharingobjectsaccounts" title="SharingObjectsAccounts">SharingObjectsAccounts</a>" : <i>[ Double, ... ]</i>,
        "<a href="#utilizationsettings" title="UtilizationSettings">UtilizationSettings</a>" : <i>[ <a href="utilizationsettingsdefinition.md">UtilizationSettingsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Logzio::Subaccount
Properties:
    <a href="#accessible" title="Accessible">Accessible</a>: <i>Boolean</i>
    <a href="#accountname" title="AccountName">AccountName</a>: <i>String</i>
    <a href="#docsizesetting" title="DocSizeSetting">DocSizeSetting</a>: <i>Boolean</i>
    <a href="#email" title="Email">Email</a>: <i>String</i>
    <a href="#maxdailygb" title="MaxDailyGb">MaxDailyGb</a>: <i>Double</i>
    <a href="#retentiondays" title="RetentionDays">RetentionDays</a>: <i>Double</i>
    <a href="#searchable" title="Searchable">Searchable</a>: <i>Boolean</i>
    <a href="#sharingobjectsaccounts" title="SharingObjectsAccounts">SharingObjectsAccounts</a>: <i>
      - Double</i>
    <a href="#utilizationsettings" title="UtilizationSettings">UtilizationSettings</a>: <i>
      - <a href="utilizationsettingsdefinition.md">UtilizationSettingsDefinition</a></i>
</pre>

## Properties

#### Accessible

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccountName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DocSizeSetting

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Email

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxDailyGb

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetentionDays

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Searchable

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharingObjectsAccounts

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UtilizationSettings

_Required_: No

_Type_: List of <a href="utilizationsettingsdefinition.md">UtilizationSettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AccountId

Returns the <code>AccountId</code> value.

#### AccountToken

Returns the <code>AccountToken</code> value.

#### Id

Returns the <code>Id</code> value.

