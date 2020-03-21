# Terraform::OPC::StorageContainer

Creates and manages a Container in the Oracle Cloud Infrastructure Storage Classic service. `storage_endpoint` must be set in the
provider or environment to manage these resources.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OPC::StorageContainer",
    "Properties" : {
        "<a href="#allowedorigins" title="AllowedOrigins">AllowedOrigins</a>" : <i>[ String, ... ]</i>,
        "<a href="#exposedheaders" title="ExposedHeaders">ExposedHeaders</a>" : <i>[ String, ... ]</i>,
        "<a href="#maxage" title="MaxAge">MaxAge</a>" : <i>Double</i>,
        "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ <a href="metadata.md">Metadata</a>, ... ]</i>,
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
    <a href="#maxage" title="MaxAge">MaxAge</a>: <i>Double</i>
    <a href="#metadata" title="Metadata">Metadata</a>: <i>
      - <a href="metadata.md">Metadata</a></i>
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

List of origins that are allowed to make cross-origin requests.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExposedHeaders

List of headers exposed to the user agent (e.g. browser) in the actual request response.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxAge

Maximum age in seconds for the origin to hold the preflight results.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

Additional object metadata headers. See [Container Metadata ](#container-metadata) below for more information.

_Required_: No

_Type_: List of <a href="metadata.md">Metadata</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the Storage Container.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrimaryKey

The primary secret key value for temporary URLs.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QuotaBytes

Maximum size of the container, in bytes.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QuotaCount

Maximum object count of the container.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReadAcls

The list of ACLs that grant read access. See [Setting Container ACLs](#setting-container-acls).

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecondaryKey

The secondary secret key value for temporary URLs.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WriteAcls

The list of ACLs that grant write access. See [Setting Container ACLs](#setting-container-acls).

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

