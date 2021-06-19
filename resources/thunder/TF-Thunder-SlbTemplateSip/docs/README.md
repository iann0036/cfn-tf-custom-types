# TF::Thunder::SlbTemplateSip

`thunder_slb_template_sip` Provides details about thunder slb template sip

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::SlbTemplateSip",
    "Properties" : {
        "<a href="#aclid" title="AclId">AclId</a>" : <i>Double</i>,
        "<a href="#aclnamevalue" title="AclNameValue">AclNameValue</a>" : <i>String</i>,
        "<a href="#algdestnat" title="AlgDestNat">AlgDestNat</a>" : <i>Double</i>,
        "<a href="#algsourcenat" title="AlgSourceNat">AlgSourceNat</a>" : <i>Double</i>,
        "<a href="#callidpersistdisable" title="CallIdPersistDisable">CallIdPersistDisable</a>" : <i>Double</i>,
        "<a href="#clientkeepalive" title="ClientKeepAlive">ClientKeepAlive</a>" : <i>Double</i>,
        "<a href="#dialogaware" title="DialogAware">DialogAware</a>" : <i>Double</i>,
        "<a href="#dropwhenclientfail" title="DropWhenClientFail">DropWhenClientFail</a>" : <i>Double</i>,
        "<a href="#dropwhenserverfail" title="DropWhenServerFail">DropWhenServerFail</a>" : <i>Double</i>,
        "<a href="#failedclientselection" title="FailedClientSelection">FailedClientSelection</a>" : <i>Double</i>,
        "<a href="#failedclientselectionmessage" title="FailedClientSelectionMessage">FailedClientSelectionMessage</a>" : <i>String</i>,
        "<a href="#failedserverselection" title="FailedServerSelection">FailedServerSelection</a>" : <i>Double</i>,
        "<a href="#failedserverselectionmessage" title="FailedServerSelectionMessage">FailedServerSelectionMessage</a>" : <i>String</i>,
        "<a href="#insertclientip" title="InsertClientIp">InsertClientIp</a>" : <i>Double</i>,
        "<a href="#interval" title="Interval">Interval</a>" : <i>Double</i>,
        "<a href="#keepserveripifmatchacl" title="KeepServerIpIfMatchAcl">KeepServerIpIfMatchAcl</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#pstngw" title="PstnGw">PstnGw</a>" : <i>String</i>,
        "<a href="#serverkeepalive" title="ServerKeepAlive">ServerKeepAlive</a>" : <i>Double</i>,
        "<a href="#serverselectionperrequest" title="ServerSelectionPerRequest">ServerSelectionPerRequest</a>" : <i>Double</i>,
        "<a href="#servicegroup" title="ServiceGroup">ServiceGroup</a>" : <i>String</i>,
        "<a href="#smpcallidrtpsession" title="SmpCallIdRtpSession">SmpCallIdRtpSession</a>" : <i>Double</i>,
        "<a href="#timeout" title="Timeout">Timeout</a>" : <i>Double</i>,
        "<a href="#usertag" title="UserTag">UserTag</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#clientrequestheader" title="ClientRequestHeader">ClientRequestHeader</a>" : <i>[ <a href="clientrequestheaderdefinition.md">ClientRequestHeaderDefinition</a>, ... ]</i>,
        "<a href="#clientresponseheader" title="ClientResponseHeader">ClientResponseHeader</a>" : <i>[ <a href="clientresponseheaderdefinition.md">ClientResponseHeaderDefinition</a>, ... ]</i>,
        "<a href="#excludetranslation" title="ExcludeTranslation">ExcludeTranslation</a>" : <i>[ <a href="excludetranslationdefinition.md">ExcludeTranslationDefinition</a>, ... ]</i>,
        "<a href="#serverrequestheader" title="ServerRequestHeader">ServerRequestHeader</a>" : <i>[ <a href="serverrequestheaderdefinition.md">ServerRequestHeaderDefinition</a>, ... ]</i>,
        "<a href="#serverresponseheader" title="ServerResponseHeader">ServerResponseHeader</a>" : <i>[ <a href="serverresponseheaderdefinition.md">ServerResponseHeaderDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::SlbTemplateSip
Properties:
    <a href="#aclid" title="AclId">AclId</a>: <i>Double</i>
    <a href="#aclnamevalue" title="AclNameValue">AclNameValue</a>: <i>String</i>
    <a href="#algdestnat" title="AlgDestNat">AlgDestNat</a>: <i>Double</i>
    <a href="#algsourcenat" title="AlgSourceNat">AlgSourceNat</a>: <i>Double</i>
    <a href="#callidpersistdisable" title="CallIdPersistDisable">CallIdPersistDisable</a>: <i>Double</i>
    <a href="#clientkeepalive" title="ClientKeepAlive">ClientKeepAlive</a>: <i>Double</i>
    <a href="#dialogaware" title="DialogAware">DialogAware</a>: <i>Double</i>
    <a href="#dropwhenclientfail" title="DropWhenClientFail">DropWhenClientFail</a>: <i>Double</i>
    <a href="#dropwhenserverfail" title="DropWhenServerFail">DropWhenServerFail</a>: <i>Double</i>
    <a href="#failedclientselection" title="FailedClientSelection">FailedClientSelection</a>: <i>Double</i>
    <a href="#failedclientselectionmessage" title="FailedClientSelectionMessage">FailedClientSelectionMessage</a>: <i>String</i>
    <a href="#failedserverselection" title="FailedServerSelection">FailedServerSelection</a>: <i>Double</i>
    <a href="#failedserverselectionmessage" title="FailedServerSelectionMessage">FailedServerSelectionMessage</a>: <i>String</i>
    <a href="#insertclientip" title="InsertClientIp">InsertClientIp</a>: <i>Double</i>
    <a href="#interval" title="Interval">Interval</a>: <i>Double</i>
    <a href="#keepserveripifmatchacl" title="KeepServerIpIfMatchAcl">KeepServerIpIfMatchAcl</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#pstngw" title="PstnGw">PstnGw</a>: <i>String</i>
    <a href="#serverkeepalive" title="ServerKeepAlive">ServerKeepAlive</a>: <i>Double</i>
    <a href="#serverselectionperrequest" title="ServerSelectionPerRequest">ServerSelectionPerRequest</a>: <i>Double</i>
    <a href="#servicegroup" title="ServiceGroup">ServiceGroup</a>: <i>String</i>
    <a href="#smpcallidrtpsession" title="SmpCallIdRtpSession">SmpCallIdRtpSession</a>: <i>Double</i>
    <a href="#timeout" title="Timeout">Timeout</a>: <i>Double</i>
    <a href="#usertag" title="UserTag">UserTag</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#clientrequestheader" title="ClientRequestHeader">ClientRequestHeader</a>: <i>
      - <a href="clientrequestheaderdefinition.md">ClientRequestHeaderDefinition</a></i>
    <a href="#clientresponseheader" title="ClientResponseHeader">ClientResponseHeader</a>: <i>
      - <a href="clientresponseheaderdefinition.md">ClientResponseHeaderDefinition</a></i>
    <a href="#excludetranslation" title="ExcludeTranslation">ExcludeTranslation</a>: <i>
      - <a href="excludetranslationdefinition.md">ExcludeTranslationDefinition</a></i>
    <a href="#serverrequestheader" title="ServerRequestHeader">ServerRequestHeader</a>: <i>
      - <a href="serverrequestheaderdefinition.md">ServerRequestHeaderDefinition</a></i>
    <a href="#serverresponseheader" title="ServerResponseHeader">ServerResponseHeader</a>: <i>
      - <a href="serverresponseheaderdefinition.md">ServerResponseHeaderDefinition</a></i>
</pre>

## Properties

#### AclId

ACL id.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AclNameValue

IPv4 Access List Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlgDestNat

Translate VIP to real server IP in SIP message when destination NAT is used.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlgSourceNat

Translate source IP to NAT IP in SIP message when source NAT is used.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CallIdPersistDisable

Disable call-ID persistence.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientKeepAlive

Respond client keep-alive packet directly instead of forwarding to server.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DialogAware

Permit system processes dialog session.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DropWhenClientFail

Drop current SIP message when select client fail.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DropWhenServerFail

Drop current SIP message when select server fail.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FailedClientSelection

Define action when select client fail.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FailedClientSelectionMessage

Send SIP message (includs status code) to server when select client fail(Format: 3 digits(1XX~6XX) space reason).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FailedServerSelection

Define action when select server fail.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FailedServerSelectionMessage

Send SIP message (includs status code) to client when select server fail(Format: 3 digits(1XX~6XX) space reason).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InsertClientIp

Insert Client IP address into SIP header.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interval

The interval of keep-alive packet for each persist connection (second).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeepServerIpIfMatchAcl

Use Real Server IP for addresses matching the ACL for a Call-Id.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

SIP Template Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PstnGw

configure pstn gw host name for tel: uri translate to sip: uri (Hostname String, default is “pstn”).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerKeepAlive

Send server keep-alive packet for every persist connection when enable conn-reuse.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerSelectionPerRequest

Force server selection on every SIP request.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceGroup

service group name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SmpCallIdRtpSession

Create the across cpu call-id rtp session.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeout

Time in minutes.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserTag

Customized tag.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

uuid of the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientRequestHeader

_Required_: No

_Type_: List of <a href="clientrequestheaderdefinition.md">ClientRequestHeaderDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientResponseHeader

_Required_: No

_Type_: List of <a href="clientresponseheaderdefinition.md">ClientResponseHeaderDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExcludeTranslation

_Required_: No

_Type_: List of <a href="excludetranslationdefinition.md">ExcludeTranslationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerRequestHeader

_Required_: No

_Type_: List of <a href="serverrequestheaderdefinition.md">ServerRequestHeaderDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerResponseHeader

_Required_: No

_Type_: List of <a href="serverresponseheaderdefinition.md">ServerResponseHeaderDefinition</a>

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

