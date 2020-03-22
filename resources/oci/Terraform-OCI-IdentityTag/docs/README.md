# Terraform::OCI::IdentityTag

This resource provides the Tag resource in Oracle Cloud Infrastructure Identity service.

Creates a new tag in the specified tag namespace.

The tag requires either the OCID or the name of the tag namespace that will contain this 
tag definition.

You must specify a *name* for the tag, which must be unique across all tags in the tag namespace
and cannot be changed. The name can contain any ASCII character except the space (_) or period (.) characters.
Names are case insensitive. That means, for example, "myTag" and "mytag" are not allowed in the same namespace.
If you specify a name that's already in use in the tag namespace, a 409 error is returned.

The tag must have a *description*. It does not have to be unique, and you can change it with
[UpdateTag](https://docs.cloud.oracle.com/iaas/api/#/en/identity/latest/Tag/UpdateTag).

The tag must have a value type, which is specified with a validator. Tags can use either a 
static value or a list of possible values. Static values are entered by a user applying the tag
to a resource. Lists are created by you and the user must apply a value from the list. Lists 
are validiated. 

* If no `validator` is set, the user applying the tag to a resource can type in a static 
value or leave the tag value empty. 
* If a `validator` is set, the user applying the tag to a resource must select from a list
of values that you supply with [EnumTagDefinitionValidator](https://docs.cloud.oracle.com/iaas/api/#/en/identity/latest/datatypes/EnumTagDefinitionValidator).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OCI::IdentityTag",
    "Properties" : {
        "<a href="#definedtags" title="DefinedTags">DefinedTags</a>" : <i>[ <a href="definedtags.md">DefinedTags</a>, ... ]</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#freeformtags" title="FreeformTags">FreeformTags</a>" : <i>[ <a href="freeformtags.md">FreeformTags</a>, ... ]</i>,
        "<a href="#iscosttracking" title="IsCostTracking">IsCostTracking</a>" : <i>Boolean</i>,
        "<a href="#isretired" title="IsRetired">IsRetired</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#tagnamespaceid" title="TagNamespaceId">TagNamespaceId</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#validator" title="Validator">Validator</a>" : <i>[ <a href="validator.md">Validator</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OCI::IdentityTag
Properties:
    <a href="#definedtags" title="DefinedTags">DefinedTags</a>: <i>
      - <a href="definedtags.md">DefinedTags</a></i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#freeformtags" title="FreeformTags">FreeformTags</a>: <i>
      - <a href="freeformtags.md">FreeformTags</a></i>
    <a href="#iscosttracking" title="IsCostTracking">IsCostTracking</a>: <i>Boolean</i>
    <a href="#isretired" title="IsRetired">IsRetired</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#tagnamespaceid" title="TagNamespaceId">TagNamespaceId</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#validator" title="Validator">Validator</a>: <i>
      - <a href="validator.md">Validator</a></i>
</pre>

## Properties

#### DefinedTags

(Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`.

_Required_: No

_Type_: List of <a href="definedtags.md">DefinedTags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

(Updatable) The description you assign to the tag during creation.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeformTags

(Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

_Required_: No

_Type_: List of <a href="freeformtags.md">FreeformTags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsCostTracking

(Updatable) Indicates whether the tag is enabled for cost tracking.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsRetired

(Updatable) Indicates whether the tag is retired. See [Retiring Key Definitions and Namespace Definitions](https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/taggingoverview.htm#Retiring).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name you assign to the tag during creation. This is the tag key definition. The name must be unique within the tag namespace and cannot be changed.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagNamespaceId

The OCID of the tag namespace.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Validator

_Required_: No

_Type_: List of <a href="validator.md">Validator</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

#### State

Returns the <code>State</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

