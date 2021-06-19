# TF::AVI::Vsdatascriptset

The VSDataScriptSet resource allows the creation and management of Avi VSDataScriptSet

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AVI::Vsdatascriptset",
    "Properties" : {
        "<a href="#createdby" title="CreatedBy">CreatedBy</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#ipreputationdbref" title="IpReputationDbRef">IpReputationDbRef</a>" : <i>String</i>,
        "<a href="#ipgrouprefs" title="IpgroupRefs">IpgroupRefs</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#poolgrouprefs" title="PoolGroupRefs">PoolGroupRefs</a>" : <i>[ String, ... ]</i>,
        "<a href="#poolrefs" title="PoolRefs">PoolRefs</a>" : <i>[ String, ... ]</i>,
        "<a href="#protocolparserrefs" title="ProtocolParserRefs">ProtocolParserRefs</a>" : <i>[ String, ... ]</i>,
        "<a href="#stringgrouprefs" title="StringGroupRefs">StringGroupRefs</a>" : <i>[ String, ... ]</i>,
        "<a href="#tenantref" title="TenantRef">TenantRef</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#datascript" title="Datascript">Datascript</a>" : <i>[ <a href="datascriptdefinition.md">DatascriptDefinition</a>, ... ]</i>,
        "<a href="#markers" title="Markers">Markers</a>" : <i>[ <a href="markersdefinition.md">MarkersDefinition</a>, ... ]</i>,
        "<a href="#ratelimiters" title="RateLimiters">RateLimiters</a>" : <i>[ <a href="ratelimitersdefinition.md">RateLimitersDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AVI::Vsdatascriptset
Properties:
    <a href="#createdby" title="CreatedBy">CreatedBy</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#ipreputationdbref" title="IpReputationDbRef">IpReputationDbRef</a>: <i>String</i>
    <a href="#ipgrouprefs" title="IpgroupRefs">IpgroupRefs</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#poolgrouprefs" title="PoolGroupRefs">PoolGroupRefs</a>: <i>
      - String</i>
    <a href="#poolrefs" title="PoolRefs">PoolRefs</a>: <i>
      - String</i>
    <a href="#protocolparserrefs" title="ProtocolParserRefs">ProtocolParserRefs</a>: <i>
      - String</i>
    <a href="#stringgrouprefs" title="StringGroupRefs">StringGroupRefs</a>: <i>
      - String</i>
    <a href="#tenantref" title="TenantRef">TenantRef</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#datascript" title="Datascript">Datascript</a>: <i>
      - <a href="datascriptdefinition.md">DatascriptDefinition</a></i>
    <a href="#markers" title="Markers">Markers</a>: <i>
      - <a href="markersdefinition.md">MarkersDefinition</a></i>
    <a href="#ratelimiters" title="RateLimiters">RateLimiters</a>: <i>
      - <a href="ratelimitersdefinition.md">RateLimitersDefinition</a></i>
</pre>

## Properties

#### CreatedBy

Creator name. Field introduced in 17.1.11,17.2.4.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

User defined description for the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpReputationDbRef

Ip reputation database that can be used by datascript functions. It is a reference to an object of type ipreputationdb. Field introduced in 20.1.3.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpgroupRefs

Uuid of ip groups that could be referred by vsdatascriptset objects. It is a reference to an object of type ipaddrgroup.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name for the virtual service datascript collection.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PoolGroupRefs

Uuid of pool groups that could be referred by vsdatascriptset objects. It is a reference to an object of type poolgroup.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PoolRefs

Uuid of pools that could be referred by vsdatascriptset objects. It is a reference to an object of type pool.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProtocolParserRefs

List of protocol parsers that could be referred by vsdatascriptset objects. It is a reference to an object of type protocolparser. Field introduced in 18.2.3. Allowed in basic edition, essentials edition, enterprise edition.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StringGroupRefs

Uuid of string groups that could be referred by vsdatascriptset objects. It is a reference to an object of type stringgroup.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantRef

It is a reference to an object of type tenant.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Datascript

_Required_: No

_Type_: List of <a href="datascriptdefinition.md">DatascriptDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Markers

_Required_: No

_Type_: List of <a href="markersdefinition.md">MarkersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RateLimiters

_Required_: No

_Type_: List of <a href="ratelimitersdefinition.md">RateLimitersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

