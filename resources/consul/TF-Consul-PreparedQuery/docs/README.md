# TF::Consul::PreparedQuery

Allows Terraform to manage a Consul prepared query.

Managing prepared queries is done using Consul's REST API. This resource is
useful to provide a consistent and declarative way of managing prepared
queries in your Consul cluster using Terraform.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Consul::PreparedQuery",
    "Properties" : {
        "<a href="#connect" title="Connect">Connect</a>" : <i>Boolean</i>,
        "<a href="#datacenter" title="Datacenter">Datacenter</a>" : <i>String</i>,
        "<a href="#ignorecheckids" title="IgnoreCheckIds">IgnoreCheckIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#near" title="Near">Near</a>" : <i>String</i>,
        "<a href="#nodemeta" title="NodeMeta">NodeMeta</a>" : <i>[ <a href="nodemetadefinition.md">NodeMetaDefinition</a>, ... ]</i>,
        "<a href="#onlypassing" title="OnlyPassing">OnlyPassing</a>" : <i>Boolean</i>,
        "<a href="#service" title="Service">Service</a>" : <i>String</i>,
        "<a href="#servicemeta" title="ServiceMeta">ServiceMeta</a>" : <i>[ <a href="servicemetadefinition.md">ServiceMetaDefinition</a>, ... ]</i>,
        "<a href="#session" title="Session">Session</a>" : <i>String</i>,
        "<a href="#storedtoken" title="StoredToken">StoredToken</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#token" title="Token">Token</a>" : <i>String</i>,
        "<a href="#dns" title="Dns">Dns</a>" : <i>[ <a href="dnsdefinition.md">DnsDefinition</a>, ... ]</i>,
        "<a href="#failover" title="Failover">Failover</a>" : <i>[ <a href="failoverdefinition.md">FailoverDefinition</a>, ... ]</i>,
        "<a href="#template" title="Template">Template</a>" : <i>[ <a href="templatedefinition.md">TemplateDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Consul::PreparedQuery
Properties:
    <a href="#connect" title="Connect">Connect</a>: <i>Boolean</i>
    <a href="#datacenter" title="Datacenter">Datacenter</a>: <i>String</i>
    <a href="#ignorecheckids" title="IgnoreCheckIds">IgnoreCheckIds</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#near" title="Near">Near</a>: <i>String</i>
    <a href="#nodemeta" title="NodeMeta">NodeMeta</a>: <i>
      - <a href="nodemetadefinition.md">NodeMetaDefinition</a></i>
    <a href="#onlypassing" title="OnlyPassing">OnlyPassing</a>: <i>Boolean</i>
    <a href="#service" title="Service">Service</a>: <i>String</i>
    <a href="#servicemeta" title="ServiceMeta">ServiceMeta</a>: <i>
      - <a href="servicemetadefinition.md">ServiceMetaDefinition</a></i>
    <a href="#session" title="Session">Session</a>: <i>String</i>
    <a href="#storedtoken" title="StoredToken">StoredToken</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#token" title="Token">Token</a>: <i>String</i>
    <a href="#dns" title="Dns">Dns</a>: <i>
      - <a href="dnsdefinition.md">DnsDefinition</a></i>
    <a href="#failover" title="Failover">Failover</a>: <i>
      - <a href="failoverdefinition.md">FailoverDefinition</a></i>
    <a href="#template" title="Template">Template</a>: <i>
      - <a href="templatedefinition.md">TemplateDefinition</a></i>
</pre>

## Properties

#### Connect

When `true` the prepared query will return connect
proxy services for a queried service.  Conditions such as `tags` in the
prepared query will be matched against the proxy service. Defaults to false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Datacenter

The datacenter to use. This overrides the
agent's default datacenter and the datacenter in the provider setup.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreCheckIds

Specifies a list of check IDs that should be
ignored when filtering unhealthy instances. This is mostly useful in an
emergency or as a temporary measure when a health check is found to be
unreliable. Being able to ignore it in centrally-defined queries can be
simpler than de-registering the check as an interim solution until the check
can be fixed.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the prepared query. Used to identify
the prepared query during requests. Can be specified as an empty string
to configure the query as a catch-all.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Near

Allows specifying the name of a node to sort results
near using Consul's distance sorting and network coordinates. The magic
`_agent` value can be used to always sort nearest the node servicing the
request.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeMeta

Specifies a list of user-defined key/value pairs that
will be used for filtering the query results to nodes with the given metadata
values present.

_Required_: No

_Type_: List of <a href="nodemetadefinition.md">NodeMetaDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OnlyPassing

When `true`, the prepared query will only
return nodes with passing health checks in the result.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Service

The name of the service to query.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceMeta

Specifies a list of user-defined key/value pairs
that will be used for filtering the query results to services with the given
metadata values present.

_Required_: No

_Type_: List of <a href="servicemetadefinition.md">ServiceMetaDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Session

The name of the Consul session to tie this query's
lifetime to.  This is an advanced parameter that should not be used without a
complete understanding of Consul sessions and the implications of their use
(it is recommended to leave this blank in nearly all cases).  If this
parameter is omitted the query will not expire.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StoredToken

The ACL token to store with the prepared
query. This token will be used by default whenever the query is executed.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

The list of required and/or disallowed tags.  If a tag is
in this list it must be present.  If the tag is preceded with a "!" then it is
disallowed.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Token

The ACL token to use when saving the prepared query.
This overrides the token that the agent provides by default.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dns

_Required_: No

_Type_: List of <a href="dnsdefinition.md">DnsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Failover

_Required_: No

_Type_: List of <a href="failoverdefinition.md">FailoverDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Template

_Required_: No

_Type_: List of <a href="templatedefinition.md">TemplateDefinition</a>

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

