# Terraform::AzureRM::StreamAnalyticsStreamInputBlob

Manages a Stream Analytics Stream Input Blob.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::StreamAnalyticsStreamInputBlob",
    "Properties" : {
        "<a href="#dateformat" title="DateFormat">DateFormat</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#pathpattern" title="PathPattern">PathPattern</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#storageaccountkey" title="StorageAccountKey">StorageAccountKey</a>" : <i>String</i>,
        "<a href="#storageaccountname" title="StorageAccountName">StorageAccountName</a>" : <i>String</i>,
        "<a href="#storagecontainername" title="StorageContainerName">StorageContainerName</a>" : <i>String</i>,
        "<a href="#streamanalyticsjobname" title="StreamAnalyticsJobName">StreamAnalyticsJobName</a>" : <i>String</i>,
        "<a href="#timeformat" title="TimeFormat">TimeFormat</a>" : <i>String</i>,
        "<a href="#serialization" title="Serialization">Serialization</a>" : <i>[ <a href="serialization.md">Serialization</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::StreamAnalyticsStreamInputBlob
Properties:
    <a href="#dateformat" title="DateFormat">DateFormat</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#pathpattern" title="PathPattern">PathPattern</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#storageaccountkey" title="StorageAccountKey">StorageAccountKey</a>: <i>String</i>
    <a href="#storageaccountname" title="StorageAccountName">StorageAccountName</a>: <i>String</i>
    <a href="#storagecontainername" title="StorageContainerName">StorageContainerName</a>: <i>String</i>
    <a href="#streamanalyticsjobname" title="StreamAnalyticsJobName">StreamAnalyticsJobName</a>: <i>String</i>
    <a href="#timeformat" title="TimeFormat">TimeFormat</a>: <i>String</i>
    <a href="#serialization" title="Serialization">Serialization</a>: <i>
      - <a href="serialization.md">Serialization</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### DateFormat

The date format. Wherever `{date}` appears in `path_pattern`, the value of this property is used as the date format instead.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the Stream Input Blob. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PathPattern

The blob path pattern. Not a regular expression. It represents a pattern against which blob names will be matched to determine whether or not they should be included as input or output to the job.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the Resource Group where the Stream Analytics Job exists. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageAccountKey

The Access Key which should be used to connect to this Storage Account.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageAccountName

The name of the Storage Account.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageContainerName

The name of the Container within the Storage Account.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StreamAnalyticsJobName

The name of the Stream Analytics Job. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeFormat

The time format. Wherever `{time}` appears in `path_pattern`, the value of this property is used as the time format instead.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Serialization

_Required_: No

_Type_: List of <a href="serialization.md">Serialization</a>

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

