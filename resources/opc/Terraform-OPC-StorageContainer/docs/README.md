# Terraform::OPC::StorageContainer

CloudFormation equivalent of opc_storage_container

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OPC::StorageContainer",
    "Properties" : {
        "<a href="#allowedorigins" title="AllowedOrigins">AllowedOrigins</a>" : <i>[ String, ... ]</i>,
        "<a href="#exposedheaders" title="ExposedHeaders">ExposedHeaders</a>" : <i>[ String, ... ]</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#maxage" title="MaxAge">MaxAge</a>" : <i>Double</i>,
        "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ &lt;a href=&#34;metadata.md&#34;&gt;Metadata&lt;/a&gt;, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#primarykey" title="PrimaryKey">PrimaryKey</a>" : <i>String</i>,
        "<a href="#quotabytes" title="QuotaBytes">QuotaBytes</a>" : <i>Double</i>,
        "<a href="#quotacount" title="QuotaCount">QuotaCount</a>" : <i>Double</i>,
        "<a href="#readacls" title="ReadAcls">ReadAcls</a>" : <i>[ String, ... ]</i>,
        "<a href="#secondarykey" title="SecondaryKey">SecondaryKey</a>" : <i>String</i>,
        "<a href="#writeacls" title="WriteAcls">WriteAcls</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OPC::StorageContainer
Properties:
    <a href="#allowedorigins" title="AllowedOrigins">AllowedOrigins</a>: <i>
      - String</i>
    <a href="#exposedheaders" title="ExposedHeaders">ExposedHeaders</a>: <i>
      - String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#maxage" title="MaxAge">MaxAge</a>: <i>Double</i>
    <a href="#metadata" title="Metadata">Metadata</a>: <i>
      - &lt;a href=&#34;metadata.md&#34;&gt;Metadata&lt;/a&gt;</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#primarykey" title="PrimaryKey">PrimaryKey</a>: <i>String</i>
    <a href="#quotabytes" title="QuotaBytes">QuotaBytes</a>: <i>Double</i>
    <a href="#quotacount" title="QuotaCount">QuotaCount</a>: <i>Double</i>
    <a href="#readacls" title="ReadAcls">ReadAcls</a>: <i>
      - String</i>
    <a href="#secondarykey" title="SecondaryKey">SecondaryKey</a>: <i>String</i>
    <a href="#writeacls" title="WriteAcls">WriteAcls</a>: <i>
      - String</i>
</pre>

## Properties

#### AllowedOrigins

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExposedHeaders

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxAge

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

_Required_: No

_Type_: List of &lt;a href=&#34;metadata.md&#34;&gt;Metadata&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrimaryKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QuotaBytes

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QuotaCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReadAcls

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecondaryKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WriteAcls

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

