# Terraform::OraclePaaS::MysqlServiceInstance Backups

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cloudstoragecontainer" title="CloudStorageContainer">CloudStorageContainer</a>" : <i>String</i>,
    "<a href="#cloudstoragepassword" title="CloudStoragePassword">CloudStoragePassword</a>" : <i>String</i>,
    "<a href="#cloudstorageusername" title="CloudStorageUsername">CloudStorageUsername</a>" : <i>String</i>,
    "<a href="#createifmissing" title="CreateIfMissing">CreateIfMissing</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#cloudstoragecontainer" title="CloudStorageContainer">CloudStorageContainer</a>: <i>String</i>
<a href="#cloudstoragepassword" title="CloudStoragePassword">CloudStoragePassword</a>: <i>String</i>
<a href="#cloudstorageusername" title="CloudStorageUsername">CloudStorageUsername</a>: <i>String</i>
<a href="#createifmissing" title="CreateIfMissing">CreateIfMissing</a>: <i>Boolean</i>
</pre>

## Properties

#### CloudStorageContainer

. Name of the Oracle Storage Cloud container used for store the backups.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudStoragePassword

Password for the Oracle Storage Cloud administrator.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudStorageUsername

Username for the Oracle Storage Cloud administrator.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateIfMissing

Specifies whether to create the container if it does not exist. Default value is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

