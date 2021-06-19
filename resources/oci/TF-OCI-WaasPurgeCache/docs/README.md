# TF::OCI::WaasPurgeCache

This resource provides the Purge Cache resource in Oracle Cloud Infrastructure Web Application Acceleration and Security service.

Performs a purge of the cache for each specified resource. If no resources are passed, the cache for the entire Web Application Firewall will be purged.
For more information, see [Caching Rules](https://docs.cloud.oracle.com/iaas/Content/WAF/Tasks/cachingrules.htm#purge).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OCI::WaasPurgeCache",
    "Properties" : {
        "<a href="#resources" title="Resources">Resources</a>" : <i>[ String, ... ]</i>,
        "<a href="#waaspolicyid" title="WaasPolicyId">WaasPolicyId</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OCI::WaasPurgeCache
Properties:
    <a href="#resources" title="Resources">Resources</a>: <i>
      - String</i>
    <a href="#waaspolicyid" title="WaasPolicyId">WaasPolicyId</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Resources

A resource to purge, specified by either a hostless absolute path starting with a single slash (Example: `/path/to/resource`) or by a relative path in which the first component will be interpreted as a domain protected by the WAAS policy (Example: `example.com/path/to/resource`).

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaasPolicyId

The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the WAAS policy.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

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

