# TF::MongoDBAtlas::LdapConfiguration

`mongodbatlas_ldap_configuration` provides an LDAP Configuration resource. This allows an LDAP configuration for an Atlas project to be crated and managed. This endpoint doesn’t verify connectivity using the provided LDAP over TLS configuration details. To verify a configuration before saving it, use the resource to [verify](https://github.com/mongodb/terraform-provider-mongodbatlas/blob/INTMDB-114/website/docs/r/ldap_verify.html.markdown) the LDAP configuration.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::MongoDBAtlas::LdapConfiguration",
    "Properties" : {
        "<a href="#authenticationenabled" title="AuthenticationEnabled">AuthenticationEnabled</a>" : <i>Boolean</i>,
        "<a href="#authorizationenabled" title="AuthorizationEnabled">AuthorizationEnabled</a>" : <i>Boolean</i>,
        "<a href="#authzquerytemplate" title="AuthzQueryTemplate">AuthzQueryTemplate</a>" : <i>String</i>,
        "<a href="#bindpassword" title="BindPassword">BindPassword</a>" : <i>String</i>,
        "<a href="#bindusername" title="BindUsername">BindUsername</a>" : <i>String</i>,
        "<a href="#cacertificate" title="CaCertificate">CaCertificate</a>" : <i>String</i>,
        "<a href="#hostname" title="Hostname">Hostname</a>" : <i>String</i>,
        "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>,
        "<a href="#usertodnmapping" title="UserToDnMapping">UserToDnMapping</a>" : <i>[ <a href="usertodnmappingdefinition.md">UserToDnMappingDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::MongoDBAtlas::LdapConfiguration
Properties:
    <a href="#authenticationenabled" title="AuthenticationEnabled">AuthenticationEnabled</a>: <i>Boolean</i>
    <a href="#authorizationenabled" title="AuthorizationEnabled">AuthorizationEnabled</a>: <i>Boolean</i>
    <a href="#authzquerytemplate" title="AuthzQueryTemplate">AuthzQueryTemplate</a>: <i>String</i>
    <a href="#bindpassword" title="BindPassword">BindPassword</a>: <i>String</i>
    <a href="#bindusername" title="BindUsername">BindUsername</a>: <i>String</i>
    <a href="#cacertificate" title="CaCertificate">CaCertificate</a>: <i>String</i>
    <a href="#hostname" title="Hostname">Hostname</a>: <i>String</i>
    <a href="#port" title="Port">Port</a>: <i>Double</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
    <a href="#usertodnmapping" title="UserToDnMapping">UserToDnMapping</a>: <i>
      - <a href="usertodnmappingdefinition.md">UserToDnMappingDefinition</a></i>
</pre>

## Properties

#### AuthenticationEnabled

Specifies whether user authentication with LDAP is enabled.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthorizationEnabled

Specifies whether user authorization with LDAP is enabled. You cannot enable user authorization with LDAP without first enabling user authentication with LDAP.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthzQueryTemplate

An LDAP query template that Atlas executes to obtain the LDAP groups to which the authenticated user belongs. Used only for user authorization. Use the {USER} placeholder in the URL to substitute the authenticated username. The query is relative to the host specified with hostname. The formatting for the query must conform to RFC4515 and RFC 4516. If you do not provide a query template, Atlas attempts to use the default value: `{USER}?memberOf?base`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BindPassword

The password used to authenticate the `bind_username`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BindUsername

The user DN that Atlas uses to connect to the LDAP server. Must be the full DN, such as `CN=BindUser,CN=Users,DC=myldapserver,DC=mycompany,DC=com`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CaCertificate

CA certificate used to verify the identify of the LDAP server. Self-signed certificates are allowed.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hostname

The hostname or IP address of the LDAP server. The server must be visible to the internet or connected to your Atlas cluster with VPC Peering.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

The port to which the LDAP server listens for client connections. Default: `636`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

The unique ID for the project to configure LDAP.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserToDnMapping

_Required_: No

_Type_: List of <a href="usertodnmappingdefinition.md">UserToDnMappingDefinition</a>

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

