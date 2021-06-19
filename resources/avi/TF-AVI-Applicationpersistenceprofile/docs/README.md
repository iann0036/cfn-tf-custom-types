# TF::AVI::Applicationpersistenceprofile

The ApplicationPersistenceProfile resource allows the creation and management of Avi ApplicationPersistenceProfile

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AVI::Applicationpersistenceprofile",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#isfederated" title="IsFederated">IsFederated</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#persistencetype" title="PersistenceType">PersistenceType</a>" : <i>String</i>,
        "<a href="#serverhmdownrecovery" title="ServerHmDownRecovery">ServerHmDownRecovery</a>" : <i>String</i>,
        "<a href="#tenantref" title="TenantRef">TenantRef</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#appcookiepersistenceprofile" title="AppCookiePersistenceProfile">AppCookiePersistenceProfile</a>" : <i>[ <a href="appcookiepersistenceprofiledefinition.md">AppCookiePersistenceProfileDefinition</a>, ... ]</i>,
        "<a href="#hdrpersistenceprofile" title="HdrPersistenceProfile">HdrPersistenceProfile</a>" : <i>[ <a href="hdrpersistenceprofiledefinition.md">HdrPersistenceProfileDefinition</a>, ... ]</i>,
        "<a href="#httpcookiepersistenceprofile" title="HttpCookiePersistenceProfile">HttpCookiePersistenceProfile</a>" : <i>[ <a href="httpcookiepersistenceprofiledefinition.md">HttpCookiePersistenceProfileDefinition</a>, ... ]</i>,
        "<a href="#ippersistenceprofile" title="IpPersistenceProfile">IpPersistenceProfile</a>" : <i>[ <a href="ippersistenceprofiledefinition.md">IpPersistenceProfileDefinition</a>, ... ]</i>,
        "<a href="#markers" title="Markers">Markers</a>" : <i>[ <a href="markersdefinition.md">MarkersDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AVI::Applicationpersistenceprofile
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#isfederated" title="IsFederated">IsFederated</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#persistencetype" title="PersistenceType">PersistenceType</a>: <i>String</i>
    <a href="#serverhmdownrecovery" title="ServerHmDownRecovery">ServerHmDownRecovery</a>: <i>String</i>
    <a href="#tenantref" title="TenantRef">TenantRef</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#appcookiepersistenceprofile" title="AppCookiePersistenceProfile">AppCookiePersistenceProfile</a>: <i>
      - <a href="appcookiepersistenceprofiledefinition.md">AppCookiePersistenceProfileDefinition</a></i>
    <a href="#hdrpersistenceprofile" title="HdrPersistenceProfile">HdrPersistenceProfile</a>: <i>
      - <a href="hdrpersistenceprofiledefinition.md">HdrPersistenceProfileDefinition</a></i>
    <a href="#httpcookiepersistenceprofile" title="HttpCookiePersistenceProfile">HttpCookiePersistenceProfile</a>: <i>
      - <a href="httpcookiepersistenceprofiledefinition.md">HttpCookiePersistenceProfileDefinition</a></i>
    <a href="#ippersistenceprofile" title="IpPersistenceProfile">IpPersistenceProfile</a>: <i>
      - <a href="ippersistenceprofiledefinition.md">IpPersistenceProfileDefinition</a></i>
    <a href="#markers" title="Markers">Markers</a>: <i>
      - <a href="markersdefinition.md">MarkersDefinition</a></i>
</pre>

## Properties

#### Description

User defined description for the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsFederated

This field describes the object's replication scope. If the field is set to false, then the object is visible within the controller-cluster and its associated service-engines. If the field is set to true, then the object is replicated across the federation. Field introduced in 17.1.3.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A user-friendly name for the persistence profile.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PersistenceType

Method used to persist clients to the same server for a duration of time or a session. Enum options - PERSISTENCE_TYPE_CLIENT_IP_ADDRESS, PERSISTENCE_TYPE_HTTP_COOKIE, PERSISTENCE_TYPE_TLS, PERSISTENCE_TYPE_CLIENT_IPV6_ADDRESS, PERSISTENCE_TYPE_CUSTOM_HTTP_HEADER, PERSISTENCE_TYPE_APP_COOKIE, PERSISTENCE_TYPE_GSLB_SITE. Allowed in basic(allowed values- persistence_type_client_ip_address,persistence_type_http_cookie) edition, essentials(allowed values- persistence_type_client_ip_address,persistence_type_http_cookie) edition, enterprise edition.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerHmDownRecovery

Specifies behavior when a persistent server has been marked down by a health monitor. Enum options - HM_DOWN_PICK_NEW_SERVER, HM_DOWN_ABORT_CONNECTION, HM_DOWN_CONTINUE_PERSISTENT_SERVER. Allowed in basic(allowed values- hm_down_pick_new_server) edition, essentials(allowed values- hm_down_pick_new_server) edition, enterprise edition.

_Required_: No

_Type_: String

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

#### AppCookiePersistenceProfile

_Required_: No

_Type_: List of <a href="appcookiepersistenceprofiledefinition.md">AppCookiePersistenceProfileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HdrPersistenceProfile

_Required_: No

_Type_: List of <a href="hdrpersistenceprofiledefinition.md">HdrPersistenceProfileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpCookiePersistenceProfile

_Required_: No

_Type_: List of <a href="httpcookiepersistenceprofiledefinition.md">HttpCookiePersistenceProfileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpPersistenceProfile

_Required_: No

_Type_: List of <a href="ippersistenceprofiledefinition.md">IpPersistenceProfileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Markers

_Required_: No

_Type_: List of <a href="markersdefinition.md">MarkersDefinition</a>

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

