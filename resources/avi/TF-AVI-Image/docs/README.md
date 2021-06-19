# TF::AVI::Image

The Image resource allows the creation and management of Avi Image

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AVI::Image",
    "Properties" : {
        "<a href="#controllerpatchname" title="ControllerPatchName">ControllerPatchName</a>" : <i>String</i>,
        "<a href="#controllerpatchuuid" title="ControllerPatchUuid">ControllerPatchUuid</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#sepatchname" title="SePatchName">SePatchName</a>" : <i>String</i>,
        "<a href="#sepatchuuid" title="SePatchUuid">SePatchUuid</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#tenantref" title="TenantRef">TenantRef</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#uberbundle" title="UberBundle">UberBundle</a>" : <i>Boolean</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#cloudinfovalues" title="CloudInfoValues">CloudInfoValues</a>" : <i>[ <a href="cloudinfovaluesdefinition.md">CloudInfoValuesDefinition</a>, ... ]</i>,
        "<a href="#controllerinfo" title="ControllerInfo">ControllerInfo</a>" : <i>[ <a href="controllerinfodefinition.md">ControllerInfoDefinition</a>, ... ]</i>,
        "<a href="#migrations" title="Migrations">Migrations</a>" : <i>[ <a href="migrationsdefinition.md">MigrationsDefinition</a>, ... ]</i>,
        "<a href="#seinfo" title="SeInfo">SeInfo</a>" : <i>[ <a href="seinfodefinition.md">SeInfoDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AVI::Image
Properties:
    <a href="#controllerpatchname" title="ControllerPatchName">ControllerPatchName</a>: <i>String</i>
    <a href="#controllerpatchuuid" title="ControllerPatchUuid">ControllerPatchUuid</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#sepatchname" title="SePatchName">SePatchName</a>: <i>String</i>
    <a href="#sepatchuuid" title="SePatchUuid">SePatchUuid</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#tenantref" title="TenantRef">TenantRef</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#uberbundle" title="UberBundle">UberBundle</a>: <i>Boolean</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#cloudinfovalues" title="CloudInfoValues">CloudInfoValues</a>: <i>
      - <a href="cloudinfovaluesdefinition.md">CloudInfoValuesDefinition</a></i>
    <a href="#controllerinfo" title="ControllerInfo">ControllerInfo</a>: <i>
      - <a href="controllerinfodefinition.md">ControllerInfoDefinition</a></i>
    <a href="#migrations" title="Migrations">Migrations</a>: <i>
      - <a href="migrationsdefinition.md">MigrationsDefinition</a></i>
    <a href="#seinfo" title="SeInfo">SeInfo</a>: <i>
      - <a href="seinfodefinition.md">SeInfoDefinition</a></i>
</pre>

## Properties

#### ControllerPatchName

Mandatory controller patch name that is applied along with this base image. Field introduced in 18.2.10, 20.1.1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ControllerPatchUuid

It references the controller-patch associated with the uber image. Field introduced in 18.2.8, 20.1.1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the image. Field introduced in 18.2.6.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SePatchName

Mandatory serviceengine patch name that is applied along with this base image. Field introduced in 18.2.10, 20.1.1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SePatchUuid

It references the service engine patch associated with the uber image. Field introduced in 18.2.8, 20.1.1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Status to check if the image is present. Enum options - SYSERR_SUCCESS, SYSERR_FAILURE, SYSERR_OUT_OF_MEMORY, SYSERR_NO_ENT, SYSERR_INVAL, SYSERR_ACCESS, SYSERR_FAULT, SYSERR_IO, SYSERR_TIMEOUT, SYSERR_NOT_SUPPORTED, SYSERR_NOT_READY, SYSERR_UPGRADE_IN_PROGRESS, SYSERR_WARM_START_IN_PROGRESS, SYSERR_TRY_AGAIN, SYSERR_NOT_UPGRADING, SYSERR_PENDING, SYSERR_EVENT_GEN_FAILURE, SYSERR_CONFIG_PARAM_MISSING, SYSERR_RANGE, SYSERR_BAD_REQUEST... Field introduced in 18.2.6.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantRef

Tenant that this object belongs to. It is a reference to an object of type tenant. Field introduced in 18.2.6.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Type of the image patch/system. Enum options - IMAGE_TYPE_PATCH, IMAGE_TYPE_SYSTEM, IMAGE_TYPE_MUST_CHECK. Field introduced in 18.2.6.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UberBundle

Status to check if the image is an uber bundle. Field introduced in 18.2.8, 20.1.1.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudInfoValues

_Required_: No

_Type_: List of <a href="cloudinfovaluesdefinition.md">CloudInfoValuesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ControllerInfo

_Required_: No

_Type_: List of <a href="controllerinfodefinition.md">ControllerInfoDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Migrations

_Required_: No

_Type_: List of <a href="migrationsdefinition.md">MigrationsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeInfo

_Required_: No

_Type_: List of <a href="seinfodefinition.md">SeInfoDefinition</a>

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

