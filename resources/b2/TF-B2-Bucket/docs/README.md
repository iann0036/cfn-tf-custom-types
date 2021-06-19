# TF::B2::Bucket

CloudFormation equivalent of b2_bucket

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::B2::Bucket",
    "Properties" : {
        "<a href="#bucketinfo" title="BucketInfo">BucketInfo</a>" : <i>[ <a href="bucketinfodefinition.md">BucketInfoDefinition</a>, ... ]</i>,
        "<a href="#bucketname" title="BucketName">BucketName</a>" : <i>String</i>,
        "<a href="#buckettype" title="BucketType">BucketType</a>" : <i>String</i>,
        "<a href="#corsrules" title="CorsRules">CorsRules</a>" : <i>[ <a href="corsrulesdefinition.md">CorsRulesDefinition</a>, ... ]</i>,
        "<a href="#defaultserversideencryption" title="DefaultServerSideEncryption">DefaultServerSideEncryption</a>" : <i>[ <a href="defaultserversideencryptiondefinition.md">DefaultServerSideEncryptionDefinition</a>, ... ]</i>,
        "<a href="#filelockconfiguration" title="FileLockConfiguration">FileLockConfiguration</a>" : <i>[ <a href="filelockconfigurationdefinition.md">FileLockConfigurationDefinition</a>, ... ]</i>,
        "<a href="#lifecyclerules" title="LifecycleRules">LifecycleRules</a>" : <i>[ <a href="lifecyclerulesdefinition.md">LifecycleRulesDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::B2::Bucket
Properties:
    <a href="#bucketinfo" title="BucketInfo">BucketInfo</a>: <i>
      - <a href="bucketinfodefinition.md">BucketInfoDefinition</a></i>
    <a href="#bucketname" title="BucketName">BucketName</a>: <i>String</i>
    <a href="#buckettype" title="BucketType">BucketType</a>: <i>String</i>
    <a href="#corsrules" title="CorsRules">CorsRules</a>: <i>
      - <a href="corsrulesdefinition.md">CorsRulesDefinition</a></i>
    <a href="#defaultserversideencryption" title="DefaultServerSideEncryption">DefaultServerSideEncryption</a>: <i>
      - <a href="defaultserversideencryptiondefinition.md">DefaultServerSideEncryptionDefinition</a></i>
    <a href="#filelockconfiguration" title="FileLockConfiguration">FileLockConfiguration</a>: <i>
      - <a href="filelockconfigurationdefinition.md">FileLockConfigurationDefinition</a></i>
    <a href="#lifecyclerules" title="LifecycleRules">LifecycleRules</a>: <i>
      - <a href="lifecyclerulesdefinition.md">LifecycleRulesDefinition</a></i>
</pre>

## Properties

#### BucketInfo

_Required_: No

_Type_: List of <a href="bucketinfodefinition.md">BucketInfoDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BucketName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BucketType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CorsRules

_Required_: No

_Type_: List of <a href="corsrulesdefinition.md">CorsRulesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultServerSideEncryption

_Required_: No

_Type_: List of <a href="defaultserversideencryptiondefinition.md">DefaultServerSideEncryptionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileLockConfiguration

_Required_: No

_Type_: List of <a href="filelockconfigurationdefinition.md">FileLockConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LifecycleRules

_Required_: No

_Type_: List of <a href="lifecyclerulesdefinition.md">LifecycleRulesDefinition</a>

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

#### BucketId

Returns the <code>BucketId</code> value.

#### Id

Returns the <code>Id</code> value.

#### Options

Returns the <code>Options</code> value.

#### Revision

Returns the <code>Revision</code> value.

