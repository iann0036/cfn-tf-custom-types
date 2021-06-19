# TF::Vault::QuotaRateLimit

Manage rate limit quotas which enforce API rate limiting using a token bucket algorithm.
A rate limit quota can be created at the root level or defined on a namespace or mount by
specifying a path when creating the quota.

See [Vault's Documentation](https://www.vaultproject.io/docs/concepts/resource-quotas) for more
information.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Vault::QuotaRateLimit",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#path" title="Path">Path</a>" : <i>String</i>,
        "<a href="#rate" title="Rate">Rate</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Vault::QuotaRateLimit
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#path" title="Path">Path</a>: <i>String</i>
    <a href="#rate" title="Rate">Rate</a>: <i>Double</i>
</pre>

## Properties

#### Name

Name of the rate limit quota.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

Path of the mount or namespace to apply the quota. A blank path configures a
global rate limit quota. For example `namespace1/` adds a quota to a full namespace,
`namespace1/auth/userpass` adds a `quota` to `userpass` in `namespace1`.
Updating this field on an existing quota can have "moving" effects. For example, updating
`auth/userpass` to `namespace1/auth/userpass` moves this quota from being a global mount quota to
a namespace specific mount quota. **Note, namespaces are supported in Enterprise only.**.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rate

The maximum number of requests at any given second to be allowed by the quota
rule. The `rate` must be positive.

_Required_: Yes

_Type_: Double

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

