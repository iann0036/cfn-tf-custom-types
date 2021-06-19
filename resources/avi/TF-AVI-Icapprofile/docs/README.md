# TF::AVI::Icapprofile

The IcapProfile resource allows the creation and management of Avi IcapProfile

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AVI::Icapprofile",
    "Properties" : {
        "<a href="#allow204" title="Allow204">Allow204</a>" : <i>Boolean</i>,
        "<a href="#buffersize" title="BufferSize">BufferSize</a>" : <i>Double</i>,
        "<a href="#buffersizeexceedaction" title="BufferSizeExceedAction">BufferSizeExceedAction</a>" : <i>String</i>,
        "<a href="#cloudref" title="CloudRef">CloudRef</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#enablepreview" title="EnablePreview">EnablePreview</a>" : <i>Boolean</i>,
        "<a href="#failaction" title="FailAction">FailAction</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#poolgroupref" title="PoolGroupRef">PoolGroupRef</a>" : <i>String</i>,
        "<a href="#previewsize" title="PreviewSize">PreviewSize</a>" : <i>Double</i>,
        "<a href="#responsetimeout" title="ResponseTimeout">ResponseTimeout</a>" : <i>Double</i>,
        "<a href="#serviceuri" title="ServiceUri">ServiceUri</a>" : <i>String</i>,
        "<a href="#slowresponsewarningthreshold" title="SlowResponseWarningThreshold">SlowResponseWarningThreshold</a>" : <i>Double</i>,
        "<a href="#tenantref" title="TenantRef">TenantRef</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#vendor" title="Vendor">Vendor</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AVI::Icapprofile
Properties:
    <a href="#allow204" title="Allow204">Allow204</a>: <i>Boolean</i>
    <a href="#buffersize" title="BufferSize">BufferSize</a>: <i>Double</i>
    <a href="#buffersizeexceedaction" title="BufferSizeExceedAction">BufferSizeExceedAction</a>: <i>String</i>
    <a href="#cloudref" title="CloudRef">CloudRef</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#enablepreview" title="EnablePreview">EnablePreview</a>: <i>Boolean</i>
    <a href="#failaction" title="FailAction">FailAction</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#poolgroupref" title="PoolGroupRef">PoolGroupRef</a>: <i>String</i>
    <a href="#previewsize" title="PreviewSize">PreviewSize</a>: <i>Double</i>
    <a href="#responsetimeout" title="ResponseTimeout">ResponseTimeout</a>: <i>Double</i>
    <a href="#serviceuri" title="ServiceUri">ServiceUri</a>: <i>String</i>
    <a href="#slowresponsewarningthreshold" title="SlowResponseWarningThreshold">SlowResponseWarningThreshold</a>: <i>Double</i>
    <a href="#tenantref" title="TenantRef">TenantRef</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#vendor" title="Vendor">Vendor</a>: <i>String</i>
</pre>

## Properties

#### Allow204

Allow icap server to send 204 response as described in rfc 3507 section 4.5. Service engine will buffer the complete request if alllow_204 is enabled. If disabled, preview_size request body will be buffered if enable_preview is set to true, and rest of the request body will be streamed to the icap server. Field introduced in 20.1.3.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BufferSize

The maximum buffer size for the http request body. If the request body exceeds this size, the request will not be checked by the icap server. In this case, the configured action will be executed and a significant log entry will be generated. Allowed values are 1-51200. Field introduced in 20.1.1. Unit is kb.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BufferSizeExceedAction

Decide what should happen if the request body size exceeds the configured buffer size. If this is set to fail open, the request will not be checked by the icap server. If this is set to fail closed, the request will be rejected with 413 status code. Enum options - ICAP_FAIL_OPEN, ICAP_FAIL_CLOSED. Field introduced in 20.1.1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudRef

The cloud where this object belongs to. This must match the cloud referenced in the pool group below. It is a reference to an object of type cloud. Field introduced in 20.1.1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

A description for this icap profile. Field introduced in 20.1.1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnablePreview

Use the icap preview feature as described in rfc 3507 section 4.5. Field introduced in 20.1.1.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FailAction

Decide what should happen if there is a problem with the icap server like communication timeout, protocol error, pool error, etc. If this is set to fail open, the request will continue, but will create a significant log entry. If this is set to fail closed, the request will be rejected with a 500 status code. Enum options - ICAP_FAIL_OPEN, ICAP_FAIL_CLOSED. Field introduced in 20.1.1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the icap profile. Field introduced in 20.1.1.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PoolGroupRef

The pool group which is used to connect to icap servers. It is a reference to an object of type poolgroup. Field introduced in 20.1.1.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreviewSize

The icap preview size as described in rfc 3507 section 4.5. This should not exceed the size supported by the icap server. If this is set to 0, only the http header will be sent to the icap server as a preview. To disable preview completely, set the enable-preview option to false. Allowed values are 0-5000. Field introduced in 20.1.1. Unit is bytes.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseTimeout

Maximum time, client's request will be paused for icap processing. If this timeout is exceeded, the request to the icap server will be aborted and the configured fail action is executed. Allowed values are 50-3600000. Field introduced in 20.1.1. Unit is milliseconds.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceUri

The path and query component of the icap url. Host name and port will be taken from the pool. Field introduced in 20.1.1.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlowResponseWarningThreshold

If the icap request takes longer than this value, this request will generate a significant log entry. Allowed values are 50-3600000. Field introduced in 20.1.1. Unit is milliseconds.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantRef

Tenant which this object belongs to. It is a reference to an object of type tenant. Field introduced in 20.1.1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vendor

The vendor of the icap server. Enum options - ICAP_VENDOR_GENERIC, ICAP_VENDOR_OPSWAT, ICAP_VENDOR_LASTLINE. Field introduced in 20.1.1.

_Required_: No

_Type_: String

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

